from custom_scripts_for_nodes.Rainbow import extract_rainbow

class rainbow:
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",)}}

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "Rainbow"

    def test(self, image):
        print(type(image))
        print(image.shape)
        rnbw = extract_rainbow()
        print(rnbw.main(image))
        #do some processing on the image, in this example I just invert it
        image = 1.0 - image
        return (image,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Rainbow": rainbow
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rainbow": "Rainbow Node"
}
