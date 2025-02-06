#tuples are lists that cannot be modded
#count & index are the only methods for tuple

list_numbers = [1, 2, 3] #list
tup_numbers = ("apple", "banana", "kiwi", "blue berry", "apple", "orange", "cherry") #tuple

apple_count = tup_numbers.count("apple")
print(f"The word apple occurs {apple_count} time(s) in the tuple")
print(tup_numbers[5]) # index 5 is orange