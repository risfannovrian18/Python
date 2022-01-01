name = input("Input your name : ")
if len(name) < 3:
    print("Name must be at least  3 Characters")
elif len(name) > 50:
    print("Name must be less than 50 Characters")
else:
    print("Name looks good")
weight = int(input('Your Weight = '))
unit = input('(L)bs or (K)g: ')
if unit.upper() =="L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")