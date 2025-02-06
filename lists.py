

names = ['joe', 'hank', 'henry', 'gus']
# print(names[0]) #joe
# print(names[1]) # hank
# print(names[2]) #henry
# print(names[3]) #gus
# print(names[:2]) #['joe', 'hank']
# print(names[:]) #copy names

#exercise 
numbers = [47, 41, 26, 94, 16, 48, 9, 31, 27]
result = 0
#find the greatest number in numbers list
for x in numbers:
    if x > result:
        result = x
print(f"The highest number is {result}")