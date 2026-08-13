import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area
radius = float(input("enter the radius of the circle: "))
result = calculate_area(radius)
print("The area of the circle is: ", result)