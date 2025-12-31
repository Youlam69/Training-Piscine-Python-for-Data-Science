import sys


def main():
    """
    A program that encodes a string into Morse code.
    Supports alphanumeric characters and spaces.
    """
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }

    try:
        # Rule: Only 1 argument allowed
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        s_input = sys.argv[1]
        encoded = []

        for char in s_input.upper():
            if char in NESTED_MORSE:
                encoded.append(NESTED_MORSE[char])
            else:
                # If character is not in dictionary (e.g. ! or @)
                raise AssertionError("the arguments are bad")

        # Join with a single space
        print(" ".join(encoded))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
