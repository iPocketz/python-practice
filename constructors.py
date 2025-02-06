

class Point:
    def __init__(self, x, y): #initialize Point
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

point1 = Point(10, 20)
# print(point1.x)

#exercise
#Person with name attribute & talk method

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hola amigo! I am {self.name}") #to receive the constructors name
        
gus = Person("Gus")
gus.talk()