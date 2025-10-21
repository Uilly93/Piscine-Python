from load_image import ft_load
import numpy as np
from PIL import Image


def ft_zoom(image: Image, box: tuple):
    """crop an image to zoom in and display its infos"""
    croped = image.crop(box)
    array = np.array(croped)
    arr_gray = array[:, :, 1]
    grayscale = Image.fromarray(arr_gray, mode="L")
    return grayscale


def main():
    box: tuple = [450, 100, 850, 500]
    try:
        arg = "animal.jpeg"
        img = Image.open(arg)
        print(ft_load(arg))
        image = ft_zoom(img, box)
        print(f"the new shape is {np.shape(np.array(image))}")
        print(np.array(image))
        image.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
