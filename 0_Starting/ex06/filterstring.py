import sys


def main():
    """
    Program that takes a string S and an integer N,
    and outputs words longer than N.
    """
    try:
        # Check if number of arguments is exactly 2 (plus script name)
        # [cite: 189]
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        # Try to convert second argument to integer [cite: 185, 189]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Words are separated by space characters [cite: 186]
        # Strings do not contain special characters [cite: 187]
        words = S.split()

        # Requirement: At least one list comprehension and
        # one lambda [cite: 188]
        # We use lambda to define the condition
        # We use list comprehension to create the final list
        result = [word for word in words if (lambda w: len(w) > N)(word)]
        print(result)

    except AssertionError as e:
        # Catch and print the assertion error [cite: 173, 189]
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    # Program must follow the main structure [cite: 172, 173]
    main()
