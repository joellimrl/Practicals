from prac07.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []
    guitars.append(Guitar("Gibson",1922,16035.40))
    guitars.append(Guitar("Some other one",2020,100))
    # while True:
    #     name = input("Name: ")
    #     if name == "":
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitars.append(Guitar(name,year,cost))
    #     print("{} ({}) : ${} added".format(name,year,cost))

    print("These are my guitars:")
    x = 1
    for each in guitars:
        if each.is_vintage():
            vintage = "(vintage)"
        else:
            vintage = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(x,each.name,each.year,each.cost,vintage))
        x += 1

main()