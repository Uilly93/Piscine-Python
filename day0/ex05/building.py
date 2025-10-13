import sys


def countOccurence(argv: list[str]) -> dict:
    """
    takes a list[str] and
    retrun a dict with all the occurence count of characters
    digits,
    lower-cases,
    upper-cases,
    ponctuations,
    spaces
    in the second string
    """
    if argv.__len__() > 2:
        raise AssertionError("AssertionError: Too many arguments")
    if argv.__len__() < 2:
        raise AssertionError(
            "AssertionError: You have to provide one argument")
    chars = {"characters": 0,
             "ponctuation": 0,
             "upper": 0,
             "digits": 0,
             "spaces": 0,
             "lower": 0, }
    for c in argv[1]:
        chars["characters"] += 1
        if c.isdigit():
            chars["digits"] += 1
        elif not c.isalnum() and not c.isspace():
            chars["ponctuation"] += 1
        elif c.islower():
            chars["lower"] += 1
        elif c.isupper():
            chars["upper"] += 1
        elif c.isspace():
            chars["spaces"] += 1
    return chars


def main():
    argv = sys.argv
    line = (input("What is the text to count?\n"))
    if line:
        argv.append(line)
    try:
        chars = countOccurence(argv)
        print(f'The text contains {chars["characters"]} characters:\
                \n{chars["upper"]} upper letters\
                \n{chars["lower"]} lower letters\
                \n{chars["ponctuation"]} punctuation marks\
                \n{chars["spaces"]} spaces\
                \n{chars["digits"]} digits')
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
