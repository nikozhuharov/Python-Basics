import math

year = input()
p = int(input())
h = int(input())

x = (48-h)*(3/4)+h+p*(2/3)

if year == "leap":
    x = x*1.15

print(math.floor(x))


