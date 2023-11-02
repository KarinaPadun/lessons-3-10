# print(), input(), int() ... built-in 1 рівень , вбудовані , які доступні одразу
# офіційні модулі та бібліотеки 2 рівень, ті які знайдемо в списку, перевірені та затвердженні
# не офіційні бібліотеки треба встановлювати

# import string ВСІ ІМПОРТИ НА ГОРІ
# from string import ascii_uppercase, ascii_letters
# from string import ascii_uppercase as alphabet
# from string import *


# alphabet = string.ascii_lowercase ( всі букви з малої алфавіту)
# alphabet = string.ascii_uppercase ( всі букви з великої алфавіту)
# ascii_letters = ascii_uppercase

# print(alphabet)

import random


# dot_1 = {
#     "x": random.randint(1,100),
#     "y": random.randint(1,100),
#     "z": random.randint(1,100),
# }
# dot_2 = {
#     "x": random.randint(1,100),
#     "y": random.randint(1,100),
#     "z": random.randint(1,100),
# }
# dot_3 = {
#     "x": random.randint(1,100),
#     "y": random.randint(1,100),
#     "z": random.randint(1,100),
# }


def adding(first_num, second_num):

    result = first_num + second_num

    return result


print(adding(2,3))


def create_dot(x_coord, y_coord, z_coord):

    dot = {
        "x": x_coord,
        "y": y_coord,
        "z": z_coord,
    }

    return dot


def forming_string_of_obj(obj_coord, obj_type):

    result = f"This is {obj_type}, coordinates are {obj_coord}"

    return result



triangle = [
    create_dot(1, 22, 44),
    create_dot(14, 222, 414),
    create_dot(14, 222, 414)
]

# printing_obj(triangle, "triangle")
#
square = [
    create_dot(1, 22, 44),
    create_dot(14, 222, 414),
    create_dot(14, 222, 414),
    create_dot(14, 222, 414),
]

# text = forming_string_of_obj(square, "square")
# print(text)