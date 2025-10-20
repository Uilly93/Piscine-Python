import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice a 2d array from start to end parameter
    and print its shape before and after slice"""
    if family.__len__() == 0:
        raise AssertionError("array empty")
    for tab in family:
        if not isinstance(tab, list):
            raise AssertionError("wrong type")
        size = family[0].__len__()
        if tab.__len__() != size:
            raise AssertionError("lists not equal")
    print(f"My shape is : {np.shape(family)}")
    result = family[start:end]
    print(f"My new shape is : {np.shape(result)}")
    return result
