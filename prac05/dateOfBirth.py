from datetime import date

people = {}

def calculate_age(born):
    today = date.today()
    return today.year - int(born[2]) - ((today.month, today.day) < (int(born[1]), int(born[0])))

for i in range(5):
    name = input("Enter name of person {}: ".format(i+1))
    dob = input("Enter date of birth for {} (DD/MM/YYYY format): ".format(name))
    while True:
        try:
            for x in range(3):
                y = int(dob.split("/")[x])
                if y > date.today().year and x == 2:
                    print("Your year is not valid!")
                    raise ValueError
                elif y > 31 and x == 0:
                    print("Your date is not valid!")
                    raise ValueError
                elif y > 12 and x == 1:
                    print("Your month is not valid!")
                    raise ValueError
            people[name] = dob.split("/")
            break
        except ValueError:
            dob = input("Please enter a valid date of birth (DD/MM/YYYY): ")
        except IndexError:
            dob = input("Please enter the full date of birth (DD/MM/YYYY): ")

for each in people:
    people[each] = calculate_age(people[each])
    print("{} is {} years old today".format(each, people[each]))