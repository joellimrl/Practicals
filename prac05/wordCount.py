user = input("Text: ")

words = {}
listOfWords = user.split(" ")
for each in listOfWords:
    if each in words:
        words[each] += 1
    else:
        words[each] = 1
longest = max(len(x) for x in words)
for each in words:
    print("{:{}} : {}".format(each, longest, words[each]))