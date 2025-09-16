from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def capstone(self):
        today=date.today()
        age=today.year_self.dob.year
        if today < data(today.year,self.dob.month,self.dob.day):
            age -=1
        return age
p1=Person("Meera", "India", date(2005, 4, 14))
print("calculated age for each person")
print("*******************************")
print("person 1 :")
print("Name : ", p1.name)
print("country : ", p1.country)
print("DOB : ", p1.dob)
print("Age : ", p1.capstone)
