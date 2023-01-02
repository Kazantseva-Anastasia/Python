PI = 3.14159


def circle_length(radius):
    a = 2 * PI * radius
    return a


def circle_area(radius):
    a = PI * (radius ** 2)
    return a


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))
