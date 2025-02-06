#type conversions
# birth_year = input("Birth year: ")
#convert user input into int
# age = 2025 - int(birth_year)
# print(age)

#exercise
user_weight = input("How heavy are you? ")
#pounds/ 2.2 = kg
kg_weight = round(int(user_weight) / 2.2, 2) #float
kg_str = str(kg_weight)
print("You weigh " + kg_str + " kilograms!")