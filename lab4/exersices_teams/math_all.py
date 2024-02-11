import math

# 1
def degree_to_radian(degree):
    return degree * (math.pi / 180)

# 2
def area_trapezoid(height, base1, base2):
    return ((base1 + base2) / 2) * height

# 3
def area_regular_polygon(sides, length):
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

# 4
def area_parallelogram(base, height):
    return base * height