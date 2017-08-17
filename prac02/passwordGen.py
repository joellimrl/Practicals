import password, random

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    length = int(input("Please enter the length of the password: "))
    upper = int(input("Please enter the number of UPPERCASE chars the password needs: "))
    lower = int(input("Please enter the number of lowercase chars the password needs: "))
    num = int(input("Please enter the number of numerals the password needs: "))
    special = int(input("Please enter the number of special chars the password needs: "))

    passGen = ""
    if length < (upper+lower+num+special):
        length = upper+lower+num+special
        print("Your specified length is too short and has been extended to accomodate the total number of characters,",length)
    while not upper == lower == num == special == 0:
        choice = random.randint(1,4)
        if choice == 1 and lower > 0:
            passGen += random.choice(LOWER)
            lower -= 1
            length -= 1
        elif choice == 2 and upper > 0:
            passGen += random.choice(UPPER)
            upper -= 1
            length -= 1
        elif choice == 3 and num > 0:
            passGen += random.choice(NUMBERS)
            num -= 1
            length -= 1
        elif choice == 4 and special > 0:
            passGen += random.choice(SPECIAL)
            special -= 1
            length -= 1
        pass
    while length > 0:
        choice = random.randint(1,4)
        if choice == 1:
            passGen += random.choice(LOWER)
        elif choice == 2:
            passGen += random.choice(UPPER)
        elif choice == 3:
            passGen += random.choice(NUMBERS)
        else:
            passGen += random.choice(SPECIAL)
        length -= 1
    print("Your password is: {}".format(passGen))
    if password.is_valid_password(passGen):
        print("Your password is strong!")
    else:
        print("Your password is not strong enough!")

main()