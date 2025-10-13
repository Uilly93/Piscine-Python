import sys


def whatIs(argv):
    """
    printing if a number is 'Odd' or 'Even'
    raising 'AssertionError' exception if wrong argument is givent to the
    function
    """
    result = {0: "Even", 1: "Odd"}
    if argv.__len__() == 2:
        arg = argv[1]
        if arg.isdigit():
            num = int(arg)
            print(f'I\'m {result[num % 2]}')
        else:
            raise AssertionError("Assertion Error: argument is not an integer")
    elif argv.__len__() > 2:
        raise AssertionError("Assertion Error: more than one argument is provided")


def main():
    try:
        whatIs(sys.argv)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
