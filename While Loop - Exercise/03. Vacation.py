excursion_money = float(input())
base_money = float(input())
i = 0
j = 0
saved_money = base_money

while True:
    text = input()
    current_money = float(input())
    j += 1
    if text == "spend":
        i += 1
        if i == 5:
            print("You can't save the money.")
            print(j)
            break
        if current_money >= saved_money:
            saved_money = 0
        else:
            saved_money -= current_money
    else:
        saved_money += current_money
        i = 0
    if saved_money >= excursion_money:
        print(f"You saved the money for {j} days.")
        break



