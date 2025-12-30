import sys


def text_counter(text: str):
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in PUNCTUATION:
            punct += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError
        if len(sys.argv) == 2:
            text_counter(sys.argv[1])
            return
        print("What is the text to count?")
        text = sys.stdin.readline()
        # Ctrl+D → empty string
        if text == "":
            return
        # Only newline → do nothing
        if text == "\n":
            return
        text_counter(text)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError")
