from prac08.guitar import Guitar

def main():
    guitars = []
    in_file = open("myguitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0],int(parts[1]),float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for each in guitars:
        print(each)
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name,year,cost))
        print("{} ({}) : ${} added".format(name,year,cost))
    out_file = open("myguitars.csv",'w')
    out_string = ""
    for each in guitars:
        out_string += "{},{},{}\n".format(each.name,str(each.year),str(each.cost))
    out_file.write(out_string)

main()