from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np


def main():
    try:
        array = ft_load("landscape.jpg")
        print(f"the shape is : {np.shape(array)}")
        print(array)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
