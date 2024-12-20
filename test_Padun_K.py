from math import pi

def area_and_perimeter(form, num_2, op):
    form = input("Write the form of the figure: ").strip().lower()

    if form == 'square': # Квадрат
        side = float(input("Write the side of the square: "))
        area = side*side
        perimeter = side*4
    elif form == 'circle':# круг
        radius = float(input("Write the radius of the circle: "))
        area = pi * radius^2
        perimeter = pi * radius * 2
    elif form == 'triangle': # треугольник
        side_1 = float(input("Write the side of the square: "))
        side_2 = float(input("Write the side of the square: "))
        side_3 = float(input("Write the side of the square: "))
        area =
        perimeter =
    elif form == 'rectangle': # прямугольник
        area =
        perimeter =

    else:
        return "Error: wrong figure"
    return area,perimeter


def area_square:
    """
    This func
    :return: square area
    """
    return a^2

