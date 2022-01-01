#input name
name =input("Input your name : ")
if len(name) < 3 :
    print("Name must be at least 3 characters")
elif len(name) > 30 :
    print("Name must be less than 30 characters")
else :
    print("Name looks good")

#currency converter
currency = int(input("Input your amount of money : "))
unit = input("input your currency (Dollar or Rupiah) : ")
if unit.upper() == "DOLLAR":
    converted = currency * 14000
    print(f"{name}, Your money is {converted} Rupiah")
else :
    converted = currency / 14000
    print(f"{name}, Your money is {converted} Dollars")