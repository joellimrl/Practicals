"""
Get into your preferred group, and work on the following:
1. Construct a read_file() mrthod that reads in a string input as filename then
return the list of data from file.
   def read_file(filename):
       .........
       return data
   calling:
       data = read_file("data.txt")
       data[0] = "2005-Q1, 0.00062"
2. Second function that cleans up the data.
   def clean_up(data):
       return data

    calling:
       data = clean_up(data)
       data[0] = [2005, "Q1", 0.00062]
3. finally display all data from main()

Names: Joel Lim, Chng Zhi Xiang, JinSup Song, Lee VernHoe
"""
def read_file(filename):
    file = open(filename,"r")
    list = []
    for lines in file:
        list.append(lines)
    list.remove(list[0])
    return list

def clean_up(data):
    newData = []
    for each in data:
        line = each.replace("-",",")
        line = line.strip().split(",")
        y = []
        for x in line:
            try:
                a = float(x)
                if a.is_integer():
                    y.append(int(a))
                else:
                    y.append(a)
            except ValueError:
                y.append(x)
        newData.append(y)
    return newData

def main():
    data = read_file("mobile-data-usage.csv")
    data = clean_up(data)
    for each in data:
        print("{:<7}{:5}{:<10}".format(each[0],each[1],each[2]))
        if each[1] == "Q4":
            print()

main()