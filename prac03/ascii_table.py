LOWER = 33
UPPER = 127

def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    code = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(code, chr(code)))

def get_number(lower, upper):
    while True:
        try:
            number = int(input("Enter a number ({}-{}):\n>>>".format(lower,upper)))
            if number in range(lower,upper+1):
                return number
            else:
                print("Please enter a number within the given range!")
        except ValueError:
            print("Please enter a valid number!")

main()