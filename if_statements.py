#Booleans
is_hot = False
is_cold = False

#if/else statements
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")


#exercise
house = 1000000
good = 0.1
bad = 0.2
good_credit = False

if good_credit:
    print(f"You will need to put down ${round(float(house) * good):,}.00")
else:
    print(f"You will need to put down ${round(float(house) * bad):,}.00")