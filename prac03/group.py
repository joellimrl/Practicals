'''
Names: Joel Lim, Chng Zhi Xiang, JinSup Song, Lee VernHoe

To get back original password:
original = newPassword.split(",")
for each in original:
    print(chr(int(int(each)/2 + 65)), end="")
'''

def askPassword():
    password = input("Please enter your password here: ")
    return password

def encodePassword(password):
    newPass = ""
    for char in password:
        newPass += str((ord(char)-65)*2)+","
    newPass = newPass[0:-1] #remove the last comma
    return newPass

def printPassword(password):
    newFile = open("secret.txt","w")
    newFile.write(password)
    newFile.close()

def main():
    password = askPassword()
    newPassword = encodePassword(password)
    printPassword(newPassword)

main()