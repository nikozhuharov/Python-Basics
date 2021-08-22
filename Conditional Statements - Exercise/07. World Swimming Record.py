# Вход
# От конзолата се четат 3 реда:
# 1. Рекордът в секунди – реално число;
# 2. Разстоянието в метри – реално число;
# 3. Времето в секунди, за което плува разстояние от 1 м. - реално число.
# Изход
# Отпечатването на конзолата зависи от резултата:
#  Ако Иван е подобрил Световния рекорд отпечатваме:
# o &quot; Yes, he succeeded! The new world record is {времето на Иван} seconds.&quot;
#  Ако НЕ е подобрил рекорда отпечатваме:
# o &quot;No, he failed! He was {недостигащите секунди} seconds slower.&quot;
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

record = float(input())
distance = float(input())
time_meter = float(input())

time_ivan = distance * time_meter + (distance//15)*12.5

if time_ivan < record:
    print(f"Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record - time_ivan):.2f} seconds slower.")



