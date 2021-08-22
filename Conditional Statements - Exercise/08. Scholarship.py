# 1. Доход в лева - реално число;
# 2. Среден успех - реално числсо;
# 3. Минимална работна заплата – реално число.

import math

income = float(input())
average = float(input())
salary = float(input())

scholarship_1 = 0
scholarship_2 = 0

if income < salary and average > 4.5:
    scholarship_1 = 0.35*salary

if average >= 5.5:
    scholarship_2 = average*25

if scholarship_1 == 0 and scholarship_2 == 0:
    print("You cannot get a scholarship!")
elif scholarship_1 > scholarship_2:
    print(f"You get a Social scholarship {math.floor(scholarship_1)} BGN")
else:
    print(f"You get a scholarship for excellent results {math.floor(scholarship_2)} BGN")




