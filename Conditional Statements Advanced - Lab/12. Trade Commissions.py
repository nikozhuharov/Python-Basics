# Град 0 ≤ s ≤ 500 500 &lt; s ≤ 1 000 1 000 &lt; s ≤ 10 000 s &gt; 10 000
# Sofia 5% 7% 8% 12%
# Varna 4.5% 7.5% 10% 13%
# Plovdiv 5.5% 8% 12% 14.5%
import sys
city = input()
sales = float(input())

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
    else:
        print("error")
        sys.exit()
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
    else:
        print("error")
        sys.exit()
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5
    else:
        print("error")
        sys.exit()
else:
    print("error")
    sys.exit()

print(f"{((commission*sales)/100):.2f}")



