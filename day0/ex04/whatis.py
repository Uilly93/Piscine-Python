import sys


def main():
    result = {0: "Even", 1: "Odd"}
    if sys.argv.__len__() == 2:
        arg = sys.argv[1]
        if arg.isdigit():
            num = int(arg)
            print(f'I\'m {result[num % 2]}')
    elif sys.argv.__len__() > 2:
        print('AssertionError: more than one argument is provided')


if __name__ == "__main__":
    main()
