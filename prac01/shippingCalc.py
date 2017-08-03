itemList = []
i = 0
choice = ""
while choice != "Q":
    itemList.append(float(input("Enter cost of item: ")))
    numberOfItems = int(input("Enter number of items: "))
    while numberOfItems <= 0:
        print("Invalid number of items!")
        numberOfItems = int(input("Enter number of items: "))
    itemList[i] = itemList[i] * numberOfItems
    choice = input("Enter Q to quit or C to continue adding items: ").upper()
    i += 1
total = 0
for i in itemList:
    total += i
if total > 100:
    total *= 0.9
    print("Your total shipping cost is",total,"including a 10% discount")
else:
    print("Your total shipping cost is",total)
