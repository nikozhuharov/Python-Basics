# 1.	Броят на дните, в които тече кампанията – цяло число;
# 2.	Броят на сладкарите – цяло число;
# 3.	Броят на тортите – цяло число;
# 4.	Броят на гофретите – цяло число;
# 5.	Броят на палачинките – цяло число.
#
# •	Торта - 45 лв.
# •	Гофрета - 5.80 лв.
# •	Палачинка – 3.20 лв.
#
days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

print((days*bakers*(cakes*45+waffles*5.80+pancakes*3.20)*7)/8)
