# •	цената на  малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.
# Вход
# От конзолата се четат 5 реда:
# 1.	Цена на ягодите в лева – реално число;
# 2.	Количество на бананите в килограми – реално число;
# 3.	Количество на портокалите в килограми – реално число;
# 4.	Количество на малините в килограми – реално число;
# 5.	Количество на ягодите в килограми – реално число.

strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

print(strawberries*strawberries_price + bananas*(strawberries_price/2)*0.2 + oranges*0.6*(strawberries_price/2) + raspberries*strawberries_price/2)



