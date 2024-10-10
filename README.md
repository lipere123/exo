<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="/docs/exo-logo-black-bg.jpg">
  <img alt="exo logo" src="/docs/exo-logo-transparent.png" width="50%" height="50%">
</picture>

exo: Run your own AI cluster at home with everyday devices. Maintained by [exo labs](https://x.com/exolabs).

<h1>
Hello people, I am lipere123. </br>
This version is tailored for my supercomputer.
<h1>

<h3>

[Discord](https://discord.gg/EUnjGpsmWw) | [Telegram](https://t.me/+Kh-KqHTzFYg3MGNk) | [X](https://x.com/exolabs)

</h3>

[![GitHub Repo stars](https://img.shields.io/github/stars/exo-explore/exo)](https://github.com/exo-explore/exo/stargazers)
[![Tests](https://dl.circleci.com/status-badge/img/circleci/TrkofJDoGzdQAeL6yVHKsg/4i5hJuafuwZYZQxbRAWS71/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/TrkofJDoGzdQAeL6yVHKsg/4i5hJuafuwZYZQxbRAWS71/tree/main)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

</div>

---

This version (exo:exo-kubelocal) need powerfull nodes to work, 6 minimums on Linux Ubuntu 22.04.
It is a version specificaly tailored for a supercomputer.
So no fancy stuff like iOS or Mac whith is usefull for mobile application for example.
Here it is more a datacenter version.
Also a limited number of model are going to be supported and AGI capable of doing action will be implemented.
All developement will be push/copy on exo:main, but here only datacenter stuff will be keeped.

<div align="center">
  <h2>Update: exo is hiring. See <a href="https://exolabs.net">here</a> for more details.</h2>
</div>

## Get Involved

exo is **experimental** software. Expect bugs early on. Create issues so they can be fixed. The [exo labs](https://x.com/exolabs) team will strive to resolve issues quickly.

We also welcome contributions from the community. We have a list of bounties in [this sheet](https://docs.google.com/spreadsheets/d/1cTCpTIp48UnnIvHeLEUNg1iMy_Q6lRybgECSFCoVJpE/edit?usp=sharing).

## Features

### Wide Model Support

exo:exo-kubelocal supports LLaMA ([tinygrad](exo/inference/tinygrad/models/llama.py)).

### Dynamic Model Partitioning

exo [optimally splits up models](exo/topology/ring_memory_weighted_partitioning_strategy.py) based on the current network topology and device resources available. This enables you to run larger models than you would be able to on any single device.

### Automatic Device Discovery

exo will [automatically discover](https://github.com/exo-explore/exo/blob/945f90f676182a751d2ad7bcf20987ab7fe0181e/exo/orchestration/standard_node.py#L154) other devices using the best method available. Zero manual configuration.

### ChatGPT-compatible API

exo provides a [ChatGPT-compatible API](exo/api/chatgpt_api.py) for running models. It's a [one-line change](examples/chatgpt_api.sh) in your application to run models on your own hardware using exo.

### Device Equality

Unlike other distributed inference frameworks, exo does not use a master-worker architecture. Instead, exo devices [connect p2p](https://github.com/exo-explore/exo/blob/945f90f676182a751d2ad7bcf20987ab7fe0181e/exo/orchestration/standard_node.py#L161). As long as a device is connected somewhere in the network, it can be used to run models.

Exo supports different [partitioning strategies](exo/topology/partitioning_strategy.py) to split up a model across devices. The default partitioning strategy is [ring memory weighted partitioning](exo/topology/ring_memory_weighted_partitioning_strategy.py). This runs an inference in a ring where each device runs a number of model layers proportional to the memory of the device.

<p>
    <picture>
        <img alt="ring topology" src="docs/ring-topology.png" width="30%" height="30%">
    </picture>
</p>


## Installation

The current recommended way to install exo is from source.

### Prerequisites

- Python>=3.12.0 is required because of [issues with asyncio](https://github.com/exo-explore/exo/issues/5) in previous versions.
- Linux (with NVIDIA card):
  - NVIDIA driver (test with `nvidia-smi`)
  - CUDA (https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#cuda-cross-platform-installation) (test with `nvcc --version`)
  - cuDNN (https://developer.nvidia.com/cudnn-downloads) (test with [link](https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html#verifying-the-install-on-linux:~:text=at%20a%20time.-,Verifying%20the%20Install%20on%20Linux,Test%20passed!,-Upgrading%20From%20Older))

### Hardware Requirements

- Normally for exo:main, the only requirement to run exo is to have enough memory across all your devices to fit the entire model into memory. For example, if you are running llama 3.1 8B (fp16), you need 16GB of memory across all devices.
Now for running this version:
  - 6 x NVIDIA RTX 4000 ADA GENERATION or more powerfull, same card on each node
  - 128Go RAM on each node

### From source

```sh
git clone https://github.com/lipere123/exo.git
cd exo
git checkout exo-kubelocal
pip install -e .
# alternatively, with venv
source install.sh
```

## Documentation

### Example Usage on Multiple MacOS Devices

#### Device 1:

```sh
exo
```

#### Device 2:
```sh
exo
```

That's it! No configuration required - exo will automatically discover the other device(s).

exo starts a ChatGPT-like WebUI (powered by [tinygrad tinychat](https://github.com/tinygrad/tinygrad/tree/master/examples/tinychat)) on http://localhost:8000

For developers, exo also starts a ChatGPT-compatible API endpoint on http://localhost:8000/v1/chat/completions. Examples with curl:

#### Llama 3.2 3B:

```sh
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
     "model": "llama-3.2-3b",
     "messages": [{"role": "user", "content": "What is the meaning of exo?"}],
     "temperature": 0.7
   }'
```

#### Llama 3.1 405B:

```sh
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
     "model": "llama-3.1-405b",
     "messages": [{"role": "user", "content": "What is the meaning of exo?"}],
     "temperature": 0.7
   }'
```

#### Llava 1.5 7B (Vision Language Model):

```sh
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
     "model": "llava-1.5-7b-hf",
     "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What are these?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "http://images.cocodataset.org/val2017/000000039769.jpg"
            }
          }
        ]
      }
    ],
     "temperature": 0.0
   }'
```

### Example Usage Linux only

You need to explicitly tell exo to use the **tinygrad** inference engine.

#### Device 1 (Linux):

```sh
exo --inference-engine tinygrad
```

#### Device 2 (Linux):

```sh
exo --inference-engine tinygrad
```

Linux devices will automatically default to using the **tinygrad** inference engine.

You can read about tinygrad-specific env vars [here](https://docs.tinygrad.org/env_vars/). 
You also need to launch with CUDA=1 DEBUG=9 for this version exo:exo-kubelocal

## Debugging

Enable debug logs with the DEBUG environment variable (0-9).

```sh
DEBUG=9 exo
```

For the **tinygrad** inference engine specifically, there is a separate DEBUG flag `TINYGRAD_DEBUG` that can be used to enable debug logs (1-6).

```sh
TINYGRAD_DEBUG=2 exo
```

## Inference Engines

exo supports the following inference engines:

- ✅ [tinygrad](exo/inference/tinygrad/inference.py)
- 🚧 [PyTorch](https://github.com/exo-explore/exo/pull/139)

## Networking Modules

- ✅ [GRPC](exo/networking/grpc)
