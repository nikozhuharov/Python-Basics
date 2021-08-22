import sys

n = int(input())
s = 0
m = -sys.maxsize

for i in range(n):
    j = int(input())
    s = s + j
    if m < j:
        m = j

if m == (s - m):
    print("Yes")
    print(f"Sum = {abs(m)}")
else:
    print("No")
    print(f"Diff = {abs(m - (s - m))}")
