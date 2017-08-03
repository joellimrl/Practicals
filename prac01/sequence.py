print("1: Show even numbers from x to y\n2: Show odd numbers from x to y\n3: Show squares from x to y\n4: Exit the program")
choice = input(">>>").upper()
while choice != "4":
    if choice == "1":
        firstNumber = int(input("Enter first number: "))
        lastNumber = int(input("Enter last number: "))
        if firstNumber % 2 == 1:
            firstNumber += 1
        for i in range(firstNumber, lastNumber+1, 2):
            print(i, end=" ")
    elif choice == "2":
        firstNumber = int(input("Enter first number: "))
        lastNumber = int(input("Enter last number: "))
        if firstNumber % 2 == 0:
            firstNumber += 1
        for i in range(firstNumber, lastNumber+1, 2):
            print(i, end=" ")
    elif choice == "3":
        firstNumber = int(input("Enter first number: "))
        lastNumber = int(input("Enter last number: "))
        for i in range(firstNumber, lastNumber+1):
            print(i,"X",i,"=",i**2)
    print("\n\n1: Show even numbers from x to y\n2: Show odd numbers from x to y\n3: Show squares from x to y\n4: Exit the program")
    choice = input(">>>").upper()
print("Thanks for using the number sequence generator.")