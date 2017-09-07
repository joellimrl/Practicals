from prac07.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES",1922,16035.40)
    another = Guitar("Another guitar",2012,5)
    guitars = [gibson,another]

    for each in guitars:
        print("{} get_age() - Got {}".format(each.name,each.get_age()))
        print("{} is_vintage() - Got {}".format(each.name,each.is_vintage()))

main()