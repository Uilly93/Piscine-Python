import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """exporting a list of height width and rgb in a list"""
    if type(path) is not str:
        raise Exception("str argument is needed")
    img = Image.open(path)
    array = np.array(img)
    print(f"the shape of {path} is {np.shape(img)}")
    return array
