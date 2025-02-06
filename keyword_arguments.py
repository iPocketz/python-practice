#positional arguments: order matter
#keyword arguments: order does not matter

def order(burger, fries):
    print(f"YOu have ordered {burger} hamburger(s) & {fries} french frie(s).")
    

order(4, 1) # positional argument
order(fries=7, burger=2) #keyword argument

