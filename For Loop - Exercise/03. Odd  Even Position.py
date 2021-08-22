# &quot;&quOddSum=&quot; + {сума на числата на нечетни позиции},
# # &quot;OddMin=&quot; + { минимална стойност на числата на нечетни позиции } / {&quot;No&quot;},
# # &quot;OddMax=&quot; + { максимална стойност на числата на нечетни позиции } / {&quot;No&quot;},
# # &quot;EvenSum=&quot; + { сума на числата на четни позиции },
# # &quot;EvenMin=&quot; + { минимална стойност на числата на четни позиции } / {&quot;No&quot;},
# # &quot;EvenMax=ot; + { максимална стойност на числата на четни позиции } / {&quot;No&quot;}

import sys
n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n+1):
    j = float(input())
    if i % 2 == 0:
        even_sum += j
        if j > even_max:
            even_max = j
        if j < even_min:
            even_min = j
    else:
        odd_sum += j
        if j > odd_max:
            odd_max = j
        if j < odd_min:
            odd_min = j

print(f"OddSum={odd_sum:.2f},")

if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")

if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")

if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")

if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")



