import sys

NESTED_MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',  ' ': '/ ',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'}


def morseTranslate(argv: list[str]):
    if argv.__len__() > 2:
        raise AssertionError("AssertionError: The arguments are bad")
    for c in argv[1]:
        if not c.isalnum() and not c.isspace():
            raise AssertionError("AssertionError: The arguments are bad")
    argv = argv[1].upper()
    newArray = [NESTED_MORSE[c] for c in argv]
    print(*newArray)


def main():
    argv = sys.argv
    try:
        morseTranslate(argv)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
