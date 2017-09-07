class Date:
    def __init__(self, day=1,month=1,year=2017):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{:02}/{:02}/{:04}".format(self.day,self.month,self.year)

    def add_days(self,n):
        days = self.day + n
        while True:
            if self.month in (1,3,5,7,8,10,12):
                if days > 31:
                    self.month += 1
                    days -= 31
                else:
                    break
            elif self.month in (4,6,9,11):
                if days > 30:
                    self.month += 1
                    days -= 30
                else:
                    break
            elif self.month == 2:
                if self.year % 4 == 0:
                    if days > 29:
                        self.month += 1
                        days -= 29
                    else:
                        break
                else:
                    if days > 28:
                        self.month += 1
                        days -= 28
                    else:
                        break
            else:
                self.year += 1
                self.month = 1
        self.day = days


myDay = Date()
print(myDay)
myDay.add_days(2)
print(myDay)
while True:
    myDay.add_days(int(input("Enter days to add: ")))
    print(myDay)