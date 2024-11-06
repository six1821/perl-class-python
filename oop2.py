# create a class called person with name, age, and gender as
# # the attribute, a constructor, a method, and an object

class Person:
    # constructor method
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"My name is {self.name}, I am {self.age} years old, and I am a {self.gender}")
# object
person1=Person("Mary",21,"female")
person1.display()
