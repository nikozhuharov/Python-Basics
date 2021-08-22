age = int(input())
price_w = float(input())
price_t = float(input())
money = 0
br = 1
toy = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money = money + br*10
        br += 1
    else:
        toy += 1

money = money - br + 1

if money + toy*price_t >= price_w:
    print(f"Yes! {(money + toy*price_t - price_w):.2f}")
else:
    print(f"No! {(price_w - (money + toy*price_t)):.2f}")



