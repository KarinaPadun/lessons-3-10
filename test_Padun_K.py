from math import pi, sqrt


def area_and_perimeter():
    form = input("Write the form of the figure (square, circle, triangle, rectangle): ").strip().lower()

    if form == 'square':
        side = float(input("Write the side of the square: "))
        area = side ** 2
        perimeter = side * 4
    elif form == 'circle':
        radius = float(input("Write the radius of the circle: "))
        area = pi * (radius ** 2)
        perimeter = pi * radius * 2
    elif form == 'triangle':
        side_1 = float(input("Write the first side of the triangle: "))
        side_2 = float(input("Write the second side of the triangle: "))
        side_3 = float(input("Write the third side of the triangle: "))
        if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
            perimeter = side_1 + side_2 + side_3
            p = perimeter / 2
            area = sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))
        else:
            return "Error: the sides do not form a valid triangle"
    elif form == 'rectangle':
        side1 = float(input("Write the first side of the rectangle: "))
        side2 = float(input("Write the second side of the rectangle: "))
        area = side1 * side2
        perimeter = 2 * (side1 + side2)
    else:
        return "Error: wrong figure"
    return f"Area: {area: .2f}, Perimeter: {perimeter: .2f}"


continue_calculating = True

while continue_calculating:
    result = area_and_perimeter()
    print(result)

    yes_or_no = input('Continue? (y/n): ').strip().lower()
    if yes_or_no != 'y':
        continue_calculating = False


