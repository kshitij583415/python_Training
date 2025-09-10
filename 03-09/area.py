# 5]. Write a Python program that calculates the area of different shapes using a function inside a function.
# Define a main function area(shape) that takes the shape type as input (circle, rectangle, or triangle).
# Inside area(), define three inner functions:
# circle_area(r) → returns area of a circle = π × r²
# rectangle_area(l, w) → returns area of a rectangle = l × w
# triangle_area(b, h) → returns area of a triangle = 0.5 × b × h
# Based on the shape given, call the appropriate inner function.


def circle_area(r):
    return 3.14 * r * r

def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

def area(shape):
    if (shape == "circle"):
        r = int(input("Enter radius: "))
        return circle_area(r)
    elif shape == "rectangle":
        l, w = map(int, input("Enter l and w: ").split())
        return rectangle_area(l, w)
    elif shape == "triangle":
        b, h = map(int, input("Enter b and h: ").split())
        return triangle_area(b, h)
    else:
        return "Invalid shape"
        
shape = input("Enter shape (rectangle/triangle/circle): ").lower()
print(area(shape))


# output
# PS C:\Users\kshitij.singh\Codes\03-09> python .\area.py
# Enter shape (rectangle/triangle/circle): rectangle
# Enter l and w: 5 6
# 30

