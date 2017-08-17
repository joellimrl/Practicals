HEXA_COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "beige": "#f5f5dc", "black": "#000000",
                     "blueviolet": "#8a2be2", "ghostwhite": "#f8f8ff", "goldenrod": "#daa520", "gray": "#bebebe", "hotpink": "#ff69b4"}

user = input("Enter a colour name: ")
while user != "":
    if user.lower() in HEXA_COLOUR_CODES:
        print("The colour code for {} is {}".format(user,HEXA_COLOUR_CODES[user.lower()]))
    else:
        print("That is not a valid colour name.")
    user = input("Enter a colour name: ")