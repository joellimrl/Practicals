"""
name = input("Please enter your name: ")
nameFile = open('name.txt','w')
print(name,file=nameFile)
nameFile.close()

nameFile = open('name.txt')
readName = nameFile.read()
print("Your name is",readName)
nameFile.close()

numberFile = open('numbers.txt')
total = 0
for line in numberFile:
    num = int(line)
    total += num
print(total)
numberFile.close()
"""

x = 5
for i in range(x):
    x = x+i
    print(x, end="")