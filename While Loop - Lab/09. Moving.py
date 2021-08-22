w = int(input())
l = int(input())
h = int(input())
boxes = 0
box = 0

space = w*l*h

while True:
    line = input()
    if line == "Done":
        print(f"{space-boxes} Cubic meters left.")
        break
    box = int(line)
    boxes += box
    if boxes > space:
        print(f"No more free space! You need {boxes-space} Cubic meters more.")
        break






