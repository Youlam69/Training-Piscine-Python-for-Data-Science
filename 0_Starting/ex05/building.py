import sys
import string

def text_counter(text: str):
    """
    Counts and prints the number of upper case, lower case, punctuation marks,
    spaces, and digits in a given string.
    """
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in string.punctuation:
            punct += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

def main():
    """
    Main entry point of the script. Handles command line arguments
    and interactive input if no arguments are provided.
    """
    try:
        # 1. Check if more than one argument
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")        
        
        # 2. Case: No argument or empty string
        if len(sys.argv) < 2 or sys.argv[1] is None or sys.argv[1] == "":
            text = input("What is the text to count?\n")
            text += "\n" # Adding newline to match standard input behavior
        # 3. Case: One argument provided
        else:
            text = sys.argv[1]

        text_counter(text)
    # 4. Handle EOFError and AssertionError in case ctrl+D is pressed

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        pass
    except KeyboardInterrupt: 
        pass


if __name__ == "__main__":
    main()