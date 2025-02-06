import random


# for i in range(3):
#     print(random.randint(10, 20)) sets the digit limit from 10-20

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
# print(leader)

#exercise
class Dice():
    def roll(self):
        print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
        
#exercise
dice1 = Dice()
dice1.roll()


#solution that is good for module flexibility
class Dice2():
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second #can use () for tuple but not needed
    

#solution
dice2 = Dice2()
print(dice2.roll())