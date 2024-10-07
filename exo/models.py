from exo.inference.shard import Shard

model_base_shards = {
  ### llama
  "llama-3.1-8b": {
    "TinygradDynamicShardInferenceEngine": Shard(model_id="mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated", start_layer=0, end_layer=0, n_layers=32),
  },
}
