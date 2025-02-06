numbers = [5, 2, 1, 7, 4, 5]
numbers.insert(0, 8) #places 8 at index 0
numbers.append(20) #20 at the end of numbers
numbers.remove(5) #removes the first occurance of 5
#numbers.clear() #empties the list
numbers.pop() #removes the last index of the list
numbers.index(2) #returns the index of the first occurance of 2
#print(7 in numbers) #boolean if 7 is in numbers list
numbers.count(5) # returns the number of occurances of 5
numbers.sort() #ascending order
numbers.reverse() #descending order
numbers2 = numbers.copy() #numbers2 is now a copy of numbers without copying

# print(numbers2)

#write a program to remove duplicates in a list
num_list = [1, 5, 8, 2, 4, 7, 3, 5, 8]
uniques = []

#easier method
for y in num_list:
    if y not in uniques:
        uniques.append(y)
print(uniques)


# # complicated method
# for x in num_list:
#     if num_list.count(x) > 1:
#         num_list.remove(x)
# #print(num_list) # [1, 2, 4, 7, 3, 5, 8]
# num_list.sort()
# #print(num_list) # [1, 2, 3, 4, 5, 7, 8]


    