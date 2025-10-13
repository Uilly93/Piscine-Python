def ft_filter(func, array):
    """
    Applies a boolean function to a list and returns the elements
    for which the function returns True.

    :param func: A function that takes an element and returns a boolean.
    :param array: A list of elements to filter.
    :return: A new list containing only the elements for which
    the function returns True.
    """
    filtered = [x for x in array if func(x)]
    return filtered


def isMajor(x):
    if x < 18:
        return False
    else:
        return True


def main():
    array = [34, 1, 40, 2, 33, 3, 56, 4, 18, 6, 15, 12, 11, 19, 27, 45]
    print(f"before filter: {array}")
    major = ft_filter(isMajor, array)
    print(f"after filter: {major}")


if __name__ == "__main__":
    main()
