l = float(input("Length?"))
w = float(input("Width?"))
h = float(input("Height?"))

thickness = 1.5
density = 2500
labor_cost = 90.64

area = l * w * h
volume = (l - 3) * (w - 3) * (h - 3)
sa = (2 * (l * h)) + (2 * (w * h)) + (2 * (h * w))

print(area)
print(volume)
print(sa) 