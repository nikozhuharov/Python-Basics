import math
type_figure = input()

if type_figure == "square":
    side = float(input())
    space = side*side
elif type_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    space = side_a*side_b
elif type_figure == "circle":
    radios = float(input())
    space = math.pi*radios*radios
elif type_figure == "triangle":
    side = float(input())
    height = float(input())
    space = (side*height)/2
print(f"{space:.3f}")
