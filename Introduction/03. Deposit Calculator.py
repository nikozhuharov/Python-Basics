# 1.	Депозирана сума – реално число;
# 2.	Срок на депозита(в месеци) – цяло число;
# 3.	Годишен лихвен процент – реално число;

deposit = float(input())
term = int(input())
interest_rate = float(input())

result = deposit+deposit*(interest_rate/100*term/12)
print(result)

