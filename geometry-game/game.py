from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def is_within_rectangle(self, rect):
        if rect.lower_left.x < self.x < rect.upper_right.x and rect.lower_left.y < self.y < rect.upper_right.y:
            return True
        return False


class Rectangle:

    def __init__(self, ll, ur):
        self.lower_left = ll
        self.upper_right = ur

    def __str__(self):
        return f"Rectangle(({self.lower_left.x},{self.lower_left.y}),({self.upper_right.x},{self.upper_right.y}))"

    def area(self):
        return (self.upper_right.x - self.lower_left.x) * (self.upper_right.y - self.lower_left.y)


rect = Rectangle(Point(randint(0, 9), randint(0, 9)),
                 Point(randint(10, 19), randint(10, 19)))

print(
    f"Rectangle coordinates: {rect.lower_left.x}, {rect.lower_left.y} and {rect.upper_right.x}, {rect.upper_right.y}")

print(f"Area of the rectange: {rect.area()}")

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
print(
    f"Your point was inside rectangle: {Point(x,y).is_within_rectangle(rect)}")
