# Helper functions for pytorch inference
# Some code coming from tinygrad but written towards pytorch

import torch
from transformers import AutoModelForCausalLM

def build_transformer(model_name: str, quantize=None, device=None):
    """
    Builds a transformer model by loading it from the Hugging Face model hub and applying 
    weight conversion, quantization, and sharding as specified.

    Args:
        model_name (str): The name of the model to load from the Hugging Face model hub.
        shard (Shard): A Shard object containing information about the model shard.
        model_size (str, optional): The size of the model to load (default is "8B").
        quantize (bool, optional): Whether to apply dynamic quantization to the model (default is None).
        device (torch.device, optional): The device to load the model onto (default is None).

    Returns:
        nn.Module: The constructed and configured transformer model.
    """
    # Load model from Hugging Face hub
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if "cuda" in str(device) else torch.float32,
        device_map="auto" if "cuda" in str(device) else None
    )

    # Quantize the model if specified
    if quantize:
        model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear})

    # Shard the model if using multiple devices
    if isinstance(device, tuple):
        for name, param in model.named_parameters():
            if "scale" in name:
                param.data = param.data.chunk(len(device), dim=0)
            elif ".attention." in name:
                param.data = param.data.chunk(len(device), dim=-1)
            elif ".feed_forward.w1." in name or ".feed_forward.w3." in name:
                param.data = param.data.chunk(len(device), dim=0)
            elif ".feed_forward." in name:
                param.data = param.data.chunk(len(device), dim=-1)
            elif "tok_embeddings.weight" in name or "output.weight" in name:
                param.data = param.data.chunk(len(device), dim=0)

    return model