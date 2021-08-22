# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
super = int(input())
price = float(input())

if super > 150:
    price = price*0.9

sum = super*price + budget*0.1

if sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {(sum-budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget-sum):.2f} leva left.")





