# Use the official Python image as the base image
FROM nvidia/cuda:11.0.3-base-ubuntu20.04

# Run update
RUN apt update

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

#Install Python

RUN apt-get install -y python3.9 
RUN apt-get install -y python3-pip
RUN apt-get install -y git

# Set the working directory inside the container
WORKDIR /app


# Copy the contents of the cloned GitHub repository to the working directory in the container
COPY ./ /app

# Install Python dependencies
RUN python3.9 -m pip install numpy==1.21.6
RUN python3.9 -m pip install -r requirements.txt
RUN python3.9 -m pip install scikit-learn==0.24.2
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN python3.9 -m pip install scikit-image
#RUN cd ./custom_nodes/comfy_controlnet_preprocessors && python3.9 install.py && cd ../
RUN cd ./custom_nodes/was-node-suite-comfyui/ && python3.9 -m pip install -r requirements.txt && cd ../
RUN cd ./custom_nodes/ComfyUI-Impact-Pack/ && python3.9 install.py && cd ../
RUN cd ./custom_nodes/comfyui_controlnet_aux/ && python3.9 -m pip install -r requirements.txt && cd ../
RUN cd ./custom_nodes/comfy_mtb/ && python3.9 -m pip install -r reqs.txt && cd ../

#Download Model Weights
RUN wget -c https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors -P ./models/checkpoints/
RUN wget -c https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors -P ./models/checkpoints/

#1.5 controlnets
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_canny_sd15v2.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_depth_sd15v2.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_sketch_sd15v2.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_style_sd14v1.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_openpose_sd14v1.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -P ./models/controlnet/
RUN wget -c https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11u_sd15_tile_fp16.safetensors -P ./models/controlnet/

#XL models use ControlNet Lora
RUN wget -c https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-canny-rank128.safetensors -P ./models/controlnet/
RUN wget -c https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-depth-rank128.safetensors -P ./models/controlnet/
RUN wget -c https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-recolor-rank128.safetensors -P ./models/controlnet/
RUN wget -c https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-sketch-rank128-metadata.safetensors -P ./models/controlnet/

#T2i XL
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-canny.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-openpose.pth -P ./models/controlnet/
RUN wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-sketch.pth -P ./models/controlnet/

RUN wget -c https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -P ./models/vae/
RUN wget -c https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors -P ./models/loras/ #SDXL offset noise lora
RUN wget -c  https://huggingface.co/XpucT/Deliberate/resolve/main/Deliberate_v2.safetensors  -P ./models/checkpoints/


#Give permission to script
RUN chmod +x ./entrypoint.sh

# Set the environment variable for GPU support
ENV NVIDIA_VISIBLE_DEVICES all

# Run the Python program when the container starts
ENTRYPOINT ["./entrypoint.sh"]
