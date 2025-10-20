from load_image import ft_load
import sys


def main():
    try:
        arg = sys.argv[1]
        print(ft_load(arg))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
