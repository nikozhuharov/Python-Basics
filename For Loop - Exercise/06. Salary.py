import sys

tabs = int(input())
salary = float(input())

for i in range(tabs):
    site = input()
    if site == "Facebook":
        salary -= 150
    if site == "Instagram":
        salary -= 100
    if site == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        sys.exit()

print(round(salary))



