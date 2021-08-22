change = float(input())
coins = 0
change = change*100
change = int(change)

while change > 0:
    if change >= 200:
        change -= 200
        coins += 1
        continue
    if change >= 100:
        change -= 100
        coins += 1
        continue
    if change >= 50:
        change -= 50
        coins += 1
        continue
    if change >= 20:
        change -= 20
        coins += 1
        continue
    if change >= 10:
        change -= 10
        coins += 1
        continue
    if change >= 5:
        change -= 5
        coins += 1
        continue
    if change >= 2:
        change -= 2
        coins += 1
        continue
    if change >= 1:
        change -= 1
        coins += 1

print(coins)
