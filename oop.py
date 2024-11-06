class Fruits:
#  constructor method
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    # method
    def display(self):
        print(f"I love eating {self.name} which costs {self.price} and is {self.color}")

# instance (object)
myobj=Fruits("banana", 50,"yellow")
myobj.display()
myobj2=Fruits("apple", 20, "red")
myobj2.display()
