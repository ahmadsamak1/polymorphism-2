class Person():
    def __init__(self, name, age):
     	self.name = name
     	self.age = age
    
    def display(self):
     	print(self.name, self.age)
    
class Student(Person):
    def __init__(self, name, age, dob):
     	self.dob = dob

     	super().__init__(name, age)
    
    def displayInfo(self):
     	print(self.name, self.age, self.dob)

obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
