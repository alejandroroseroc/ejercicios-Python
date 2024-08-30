class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Animal[name={self.name}]"

class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self):
        return f"Mammal[{super().__str__()}]"

class Cat(Mammal):
    def __init__(self, name: str):
        super().__init__(name)

    def greets(self):
        print("Meow")

    def __str__(self):
        return f"Cat[{super().__str__()}]"
class Dog(Mammal):
    def __init__(self, name: str):
        super().__init__(name)

    def greets(self, another_dog=None):
        if another_dog is None:
            print("Woof")
        else:
            print("Wooooof")

    def __str__(self):
        return f"Dog[{super().__str__()}]"



animal = Animal("Generic Animal")
print(animal) 

mammal = Mammal("Generic Mammal")
print(mammal) 

cat = Cat("Whiskers")
print(cat) 
cat.greets()  

dog = Dog("Rex")
print(dog) 
dog.greets() 
dog.greets(dog)  
