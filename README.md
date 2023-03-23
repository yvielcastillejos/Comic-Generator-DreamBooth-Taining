## To Run with colab
Please use this colab link for dreambooth training on colab:
https://colab.research.google.com/drive/1cN59N1RGyHwCYkPmbretBz1jTEH7FYQF#scrollTo=AsWk2MBz1RdO

## Login to Hugging face

You need to accept the model license before downloading or using the Stable Diffusion weights. Please, visit the [model card](https://huggingface.co/runwayml/stable-diffusion-v1-5), read the license and tick the checkbox if you agree. You have to be a registered user in 🤗 Hugging Face Hub, and you'll also need to use an access token for the code to work.

1. Get your token from https://huggingface.co/settings/tokens
2. `mkdir -p ~/.huggingface`
3. HUGGINGFACE_TOKEN =
4. `echo -n "{HUGGINGFACE_TOKEN}" > ~/.huggingface/token`

## Install the xformers based on the gpu that is used:

T4:
  `pip install -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/precompiled/T4/xformers-0.0.13.dev0-py3-none-any.whl`

P100:
  `pip install -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/precompiled/P100/xformers-0.0.13.dev0-py3-none-any.whl`

V100:
  `pip install -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/precompiled/V100/xformers-0.0.13.dev0-py3-none-any.whl`

A100:
  `pip install -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/precompiled/A100/xformers-0.0.13.dev0-py3-none-any.whl`
