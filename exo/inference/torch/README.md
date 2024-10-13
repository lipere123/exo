# PyTorch & HuggingFace inference engine

## Tech

Tested on

```bash
# Laptop/PC
Distributor ID: Pop
Description:    Pop!_OS 22.04 LTS
Release:        22.04
Codename:       jammy
CUDA Version: 12.4 
Nvidia Driver Version: 550.107.02

GPU 1: Nvidia GeForce RTX 3060 6GB Laptop
```
```bash
# Server
Distributor ID: Pop
Description:    Pop!_OS 22.04 LTS
Release:        22.04
Codename:       jammy
CUDA Version:   12.4
Nvidia Driver Version: 550.90.07

GPU 1: NVIDIA T1000 8GB
GPU 2: NVIDIA Quadro M2000 4GB
GPU 3: NVIDIA Quadro M2000 4GB
GPU 4: NVIDIA Quadro P400 2GB
GPU 5: NVIDIA Quadro P400 2GB 
```


## Notes/Issues
### 10/10/2024
- To select a pytorch device via environment variables, set the variable TORCH_DEVICE
  - XLA is currently not installed and will need to be added to inference.py, looking into doing this on a TPU VM
  - With pytorch, CUDA and ROCm are the same so specifying CUDA also enables ROCm support. See this [post](https://github.com/pytorch/pytorch/issues/55223#issuecomment-812587373)
  - Looking into adding mobile device support properly
- If device is not CPU the data type defaults to float32 else float16.

### 10/13/2024
Still working on split model development (see test_split_model.py). Right now, it seems to do it but still transformers is loading more in the RAM and GPU as it loads up a larger models (causing an OOM). Will research and add to next update. Right now, tests are added and are in development.
