import json
from urllib import request, parse
import random

#this is the ComfyUI api prompt format. If you want it for a specific workflow you can copy it from the prompt section
#of the image metadata of images generated with ComfyUI
#keep in mind ComfyUI is pre alpha software so this format will change a bit.

#this is the one for the default workflow
prompt_text = """


{"3": {"inputs": {"seed": 160913364876129, "steps": 16, "cfg": 6.0, "sampler_name": "uni_pc", "scheduler": "normal", "denoise": 1.0, "model": ["14", 0], "positive": ["10", 0], "negative": ["7", 0], "latent_image": ["5", 0]}, "class_type": "KSampler"}, "5": {"inputs": {"width": 512, "height": 512, "batch_size": 1}, "class_type": "EmptyLatentImage"}, "6": {"inputs": {"text": "(solo) girl (flat chest:0.9), (fennec ears:1.1)\u00a0 (fox ears:1.1), (blonde hair:1.0), messy hair, sky clouds, standing in a grass field, (chibi), blue eyes", "clip": ["14", 1]}, "class_type": "CLIPTextEncode"}, "7": {"inputs": {"text": "(hands), text, error, cropped, (worst quality:1.2), (low quality:1.2), normal quality, (jpeg artifacts:1.3), signature, watermark, username, blurry, artist name, monochrome, sketch, censorship, censor, (copyright:1.2), extra legs, (forehead mark) (depth of field) (emotionless) (penis)", "clip": ["14", 1]}, "class_type": "CLIPTextEncode"}, "8": {"inputs": {"samples": ["3", 0], "vae": ["13", 0]}, "class_type": "VAEDecode"}, "9": {"inputs": {"filename_prefix": "ComfyUI", "images": ["8", 0]}, "class_type": "SaveImage"}, "10": {"inputs": {"strength": 0.8999999999999999, "conditioning": ["6", 0], "control_net": ["12", 0], "image": ["11", 0]}, "class_type": "ControlNetApply"}, "11": {"inputs": {"image": "ComfyUI_00005_ (1).png", "choose file to upload": "image"}, "class_type": "LoadImage", "is_changed": ["7657ee164339745ea7b5300e55a7655f0404fbb5a0a61d990748027a19e2f178"]}, "12": {"inputs": {"control_net_name": "control_v11p_sd15_canny_fp16.safetensors"}, "class_type": "ControlNetLoader"}, "13": {"inputs": {"vae_name": "vae-ft-mse-840000-ema-pruned.safetensors"}, "class_type": "VAELoader"}, "14": {"inputs": {"ckpt_name": "sd-v1-4.ckpt"}, "class_type": "CheckpointLoaderSimple"}}
"""

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)


prompt = json.loads(prompt_text)
#set the text prompt for our positive CLIPTextEncode
prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

#set the seed for our KSampler node
prompt["3"]["inputs"]["seed"] = 5


queue_prompt(prompt)