#Parent class
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("woof!")
     
        
class Cat(Mammal):
    def meow(self):
        print("RAWR!")

cat1 = Cat()
cat1.meow()