from num2words import num2words

#dictionary key/value pair
#no duplicate keys
user = {
    'name': "John",
    'email': "john@gmail.com",
    'age': 52
}

# print(user.get("birthdate")) #use the get to avoid error if not present
# print(user.get("birthdate", "Jan 3 1943")) #comma to insert default value
# user['birthdate'] = "Aug 7 2021" #assign a new key/value 
# print(user["birthdate"])
# print(user['age'])

#convert numbers into words:
#using num2words library
num = 1843
num_word = num2words(num)
# print(num_word)

#print phone number into words & ! as default if not a number
phone = input("Phone: ") #user input
#word replacement for each digit
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
#new output array
output = ""
for x in phone:#loop
    output += digits_mapping.get(x, "!") + " "#append each word with a space included
print(output) #print the outcome