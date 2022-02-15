from calendar import c
from random import randint
import turtle


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


class GUIRectangle(Rectangle):
    def draw(self, canvas):
        x_dist = self.upper_right.x - self.lower_left.x
        y_dist = self.upper_right.y - self.lower_left.y
        canvas.penup()
        canvas.goto(self.lower_left.x, self.lower_left.y)
        canvas.pendown()
        canvas.forward(x_dist)
        canvas.left(90)
        canvas.forward(y_dist)
        canvas.left(90)
        canvas.forward(x_dist)
        canvas.left(90)
        canvas.forward(y_dist)


class GUIPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


gui_rect = GUIRectangle(Point(randint(0, 100), randint(0, 100)),
                        Point(randint(200, 300), randint(200, 300)))


print(
    f"Rectangle coordinates: {gui_rect.lower_left.x}, {gui_rect.lower_left.y} and {gui_rect.upper_right.x}, {gui_rect.upper_right.y}")

print(f"Area of the rectangle: {gui_rect.area()}")


x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

gui_point = GUIPoint(x, y)

print(
    f"Your point was inside rectangle: {gui_point.is_within_rectangle(gui_rect)}")

canvas = turtle.Turtle()
gui_rect.draw(canvas)
gui_point.draw(canvas)

turtle.done()
