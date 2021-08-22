days = int(input())
room = input()
rate = input()

if room == "apartment":
    price = 25
    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    else:
        discount = 0.5

if room == "president apartment":
    price = 35
    if days < 10:
        discount = 0.1
    elif 10 <= days <= 15:
        discount = 0.15
    else:
        discount = 0.2

if room == "room for one person":
    price = 18
    discount = 0


result = price*(days-1)*(1-discount)

if rate == "positive":
    result = result*1.25
else:
    result = result*0.9

print(f"{result:.2f}")

