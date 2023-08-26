import folder_paths
import comfy.sd


class Tiled_CheckpointLoader:
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             "tile": ("INT", {"default": 0, "min": 0, "max": 1})}}
        
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")    
        
    FUNCTION = "tiled_load_checkpoint"

    CATEGORY = "custom loader"
    
    

    def tiled_load_checkpoint(self, ckpt_name, tile,output_vae=True, output_clip=True):    
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        if tile == 1:
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"),tile=True)
        else:
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"),tile=False)
        return out
    
NODE_CLASS_MAPPINGS = {
    "Custom Loader": Tiled_CheckpointLoader
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Custom Loader": "Tiled Custom Loader"
}