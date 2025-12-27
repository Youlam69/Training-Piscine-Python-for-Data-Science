import sys
# Import ft_filter li ghadi t-sawb f Part 1
from ft_filter import ft_filter

def main():
    """Main function for filtering strings by length."""
    try:
        # 1. Check arguments count (khass y-kounou 2 + smiyt l-file)
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
            
        # 2. Check types
        # Argument 1 (S) khass ykoun string, Argument 2 (N) khass ykoun integer
        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # 3. Split string into words
        words = S.split()

        # 4. Logic wuth List Comprehension and Lambda 
        

        # Hna khass t-khdem b ft_filter li sawbti
        result = [word for word in words if (lambda w: len(w) > N)(word)]
        
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()