import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """exporting a list of height width and rgb in a list"""
    if type(path) is not str:
        raise Exception("str argument is needed")
    img = Image.open(path)
    array = np.array(img)
    return array
