import sys
poor_grades = int(input())
i = 0
j = 0
average_grade = 0
sum_grade = 0

while i < poor_grades:
    name = input()
    if name == "Enough":
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {j}")
        print("Last problem: "+name_2)
        sys.exit()
    grade = int(input())
    if grade <= 4:
        i += 1
    j = j + 1
    sum_grade += grade
    average_grade = sum_grade/j
    name_2 = name

print(f"You need a break, {i} poor grades.")




