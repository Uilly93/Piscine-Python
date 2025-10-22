import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    arr_invert = array.copy()
    arr_invert = 255 - arr_invert
    image = Image.fromarray(arr_invert)
    image.show()
    return arr_invert


def ft_red(array: np.ndarray) -> np.ndarray:
    """apply red filter to image"""
    arr_red = array.copy()
    arr_red[:, :, 1] = 0
    arr_red[:, :, 2] = 0
    image = Image.fromarray(arr_red)
    image.show()
    return arr_red


def ft_green(array: np.ndarray) -> np.ndarray:
    """apply green filter to image"""
    arr_green = array.copy()
    arr_green[:, :, 0] = 0
    arr_green[:, :, 2] = 0
    image = Image.fromarray(arr_green)
    image.show()
    return arr_green


def ft_blue(array: np.ndarray) -> np.ndarray:
    # your code here
    """apply blue filter to image"""
    arr_blue = array.copy()
    arr_blue[:, :, 0] = 0
    arr_blue[:, :, 1] = 0
    image = Image.fromarray(arr_blue)
    image.show()
    return arr_blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """apply grey filter to image"""
    arr_grey = array.copy()
    arr_grey = arr_grey[:, :, 1]
    image = Image.fromarray(arr_grey)
    image.show()
    return arr_grey
