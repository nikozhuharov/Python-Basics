# 1.	Дължина в см – цяло число
# 2.	Широчина в см – цяло число
# 3.	Височина в см – цяло число
# 4.	Процент зает обем – реално число

length = int(input())
width = int(input())
height = int(input())
percent = float(input())

print(((length*width*height)/1000)*(1-percent/100))
