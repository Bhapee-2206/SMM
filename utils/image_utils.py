from PIL import Image
import numpy as np

def analyze_image_mood(image_path):

    img = Image.open(image_path)
    img = img.resize((100,100))

    pixels = np.array(img)

    brightness = pixels.mean()

    r = pixels[:,:,0].mean()
    g = pixels[:,:,1].mean()
    b = pixels[:,:,2].mean()

    if brightness > 170:
        return "happy and energetic"

    elif brightness < 90:
        return "sad and reflective"

    elif r > g and r > b:
        return "excited and adventurous"

    else:
        return "calm and neutral"