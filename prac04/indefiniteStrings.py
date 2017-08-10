strings = []
repeated = []
x = "wat"
while x != "":
    x = input("Enter string: ")
    strings.append(x)
for i in range(len(strings)):
    for x in range(i,len(strings)):
        if i == x:
            continue
        elif strings[i] == strings[x] and strings[i] not in repeated:
            repeated.append(strings[i])
if repeated == []:
    print("No repeated strings entered.")
else:
    print("Strings repeated: {}".format(repeated[0]), end="")
    for y in repeated[1:]:
        print(",",repeated[y], end="")