c_1 = int(input())
c_2 = int(input())
c_3 = int(input())

c_sum = c_1 + c_2 + c_3

minutes = c_sum // 60
seconds = c_sum % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")








