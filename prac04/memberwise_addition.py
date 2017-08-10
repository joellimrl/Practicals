def main():
    list1 = []
    list2 = []
    count = 1
    while True:
        try:
            x = int(input("Enter number: "))
            if count == 1:
                list1.append(x)
            else:
                list2.append(x)
        except ValueError:
            if count == 1:
                print("Moving on to other list.")
                count += 1
            else:
                print("Finished with both lists")
                break
    print(memberwiseAddition(list1,list2))

def memberwiseAddition(list1,list2):
    counter = 0
    newList = []
    if len(list2)>len(list1):
        for each in list1:
            newList.append(each+list2[counter])
            counter+=1
        for x in range(len(list1),len(list2)):
            newList.append(list2[x])
    else:
        for each in list2:
            newList.append(each+list1[counter])
            counter+=1
        for x in range(len(list2),len(list1)):
            newList.append(list1[x])
    return newList

main()
