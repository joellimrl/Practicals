list1 = []
list2 = []

for x in range(3):
    list1.append(input("Enter key: "))
    list2.append(input("Enter value: "))


def listsToDict(list1,list2):
    dictTotal = {}
    for y in range(len(list1)):
        dictTotal[list1[y]] = list2[y]
    return dictTotal
