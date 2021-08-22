number = float(input())
unit_1 = input()
unit_2 = input()

if unit_1 == "mm":
    if unit_2 == "cm":
        number = number/10
    else:
        number = number/1000
elif unit_1 == "cm":
    if unit_2 == "mm":
        number = number*10
    else:
        number = number/100
else:
    if unit_2 == "mm":
        number = number*1000
    else:
        number = number*100

print(f"{number:.3f}")






