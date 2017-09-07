from operator import attrgetter

class Person:
    def __init__(self, first, last, age=1):
        self.firstName = first
        self.lastName = last
        self.age = age

    def __str__(self):
        return "{} {} is {} years old".format(self.firstName,self.lastName,self.age)

    def get_age(self):
        return self.age

def main():
    people = []
    people.append(Person("Bob","Jesus",20))
    people.append(Person("WOOO","WEEE",110))
    people.append(Person("Why","not",211))
    people.append(Person("Young","boy",1))
    people.sort(key=attrgetter('age'))

    for each in people:
        print("{:5} {:5}: {} years old".format(each.firstName, each.lastName, each.age))

main()