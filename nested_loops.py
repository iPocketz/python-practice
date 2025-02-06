#loop inside a loop

# for x in range(4):
    
#     for y in range(4):
#         print(f'({x}, {y})')

#exercise
numbers = [1, 1, 1, 1, 5] #L
numbers2 = [5, 2, 5, 2, 2] #F

#easy mode:
# for x in numbers:
#     print("x" * x)

#nested loop mode
for x in numbers:
    for _ in range(x):
        print("x", end="")
    print()