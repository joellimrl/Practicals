import random

def main():
    num = []
    sameNumber = []

    count = int(input("How many quick picks? "))
    for i in range(count):
        for j in range(6):
            x = random.randint(1,45)
            while x in sameNumber:
                x = random.randint(1,45)
            sameNumber.append(x)
            num.append(x)
        num.sort()
        for j in range(6):
            print(num[j],end=" ")
        print()
        num = []
        sameNumber = []

main()