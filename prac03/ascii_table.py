LOWER = 33
UPPER = 127

"""
char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char,ord(char)))
code = int(input("Enter a number between {} and {}: ".format(LOWER,UPPER)))
while code < LOWER or code > UPPER:
    code = int(input("Please re-enter a number between {} and {}: ".format(LOWER,UPPER)))
print("The character for {} is {}".format(code, chr(code)))
"""

columns = int(input("How many columns would you like: "))
split = 93 // columns
count = 0
lower = LOWER
while lower < split+LOWER+1:
    for i in range(lower,UPPER,split+1):
        print("{:>3}   {:20}".format(i,chr(i)),end="")
        count += 1
        if count == columns:
            count = 0
            break
    lower += 1
    count = 0
    print()