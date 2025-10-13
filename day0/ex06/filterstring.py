from ft_filter import ft_filter
import sys


def filterString(argv: list[str]):
    if argv.__len__() != 3 or not argv[2].isdigit():
        raise AssertionError("AssertionError: The arguments are bad")
    array = argv[1].split()
    condition = int(argv[2])
    return ft_filter(lambda check: check.__len__() >= condition, array)


def main():
    try:
        newArray = filterString(sys.argv)
        print(newArray)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
