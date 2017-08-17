people = {}
year = []

for i in range(5):
    name = input("Enter name of person {}: ".format(i+1))
    dob = input("Enter date of birth for {} (DD/MM/YYYY format): ".format(name))
    while True:
        try:
            year.append(dob.split("/"))
            people[name] = dob
            break
        except ValueError:
            print("Please enter a valid date of birth (DD/MM/YYYY): ")
            dob = input()

print(people)
print(year)