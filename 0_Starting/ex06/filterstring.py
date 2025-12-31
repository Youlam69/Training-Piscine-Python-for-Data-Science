import sys
from ft_filter import ft_filter


def main():
    """
    Program that takes a string S and an integer N,
    and outputs words longer than N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s_input = sys.argv[1]
        try:
            n_input = int(sys.argv[2])
        except ValueError:
            # Type of argument is wrong
            raise AssertionError("the arguments are bad")

        # Words are separated by space characters
        words = s_input.split()
        result = [wrd for wrd in ft_filter(lambda w: len(w) > n_input, words)]
        print(result)

    except AssertionError as e:
        # Catch and print the assertion error
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    # No code in the global scope
    main()
