import numpy as np
from load_image import ft_load
from PIL import Image


def ft_zoom(image: Image, box: tuple):
    """crop an image to zoom in and display its infos"""
    croped = image.crop(box)
    array = np.array(croped)
    arr_gray = array[:, :, 1]
    grayscale = Image.fromarray(arr_gray, mode="L")
    return grayscale


def ft_rotate(image: Image):
    """return the rotated image at 90 degres counterclockwise"""
    array = np.array(image)
    rows = len(array)
    cols = len(array[0])
    rotated = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated[cols - j - 1][i] = array[i][j]
    transposed = np.array(rotated)
    return Image.fromarray(transposed)


def main():
    try:
        array = ft_load("animal.jpeg")
        zoomed = ft_zoom(Image.fromarray(array), [450, 100, 850, 500])
        print(f"the shape is : {np.shape(np.array(zoomed))}")
        print(np.array(zoomed))
        newImage: Image = ft_rotate(zoomed)
        print(f"the shape after Traspose is : {np.shape(np.array(newImage))}")
        print(np.array(newImage))
        newImage.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
