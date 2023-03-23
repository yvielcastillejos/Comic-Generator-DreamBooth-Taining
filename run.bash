#! /bin/sh
WGET1 = 'wget -q https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py'
$WGET1
wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
pip install -q -U --pre triton
cd /content/
pip install -r requirements.txt
wget https://github.com/TheLastBen/fast-stable-diffusion/raw/main/Dreambooth/Deps
mv Deps Deps.7z
7z x Deps.7z
cp -r /content/usr/local/lib/python3.7/dist-packages /usr/local/lib/python3.7/
rm Deps.7z
rm -r /content/usr