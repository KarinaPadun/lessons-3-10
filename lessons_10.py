# default values
# *args **kwargs
# types anotation in def

# створити у функції більш коротке імя , зовнішні змінні - більш розширенні
# дебаг  - це виявлення помилок , перевірка
# всі обовязкові елементи спочатку , а потм дефолтні

# file handling
# context manager

# *args - аргументи
# **kwargs - ключевое слово, по ключу

# *args **kwargs
# def test_def(*args, **kwargs): - 1 зірочка аргумент, 2 зірочки -кваргс
#     print(args)
#     for arg in args: - розібрало в стопчик
#         print(arg)

# (*args, **kwargs) - летить як кортеж і дікт

#     print(kwargs)
#     for kwarg in kwargs: працює як словник
#         print(kwarg, kwargs[kwarg])
#
# test_def(1,2,3,4, key=1, value=2) - 4 елементи кортежами, між дефолт значеннями і аргументом немає пробелу
# КЛЮЧ - ЗНАЧЕННЯ , ЯК СЛОВНИК ДРУКУЄ

# def square_area(side_length: float, debug_mod: bool = False) -> float: -types anotation АНОСТАЦІЯ ТИПІВ ,це показник
# який дає інформацію про те , який тип данних буде летіти в аргументах і який тип данних буде повертатись
# необовязково , для зручності
# ніяк не буде протидіять але попередить

# debug_mod: bool = False - правильний запис, дефолт значення - тип - значення


#     area = side_length ** 2
#
#     if debug_mod:
#         print("!!!!!!!!area=", area)
#
#     return area
#
#
# print(square_area(2, True))



###########################################################################################

# 1 variant

# filename = "homework/lesson_4" - шлях
# my_file = open(filename, 'r')               #'r' - read, 'w' - write, 'rb' - read binary, 'wb' - write binary
# data = my_file.read()
# my_file.close()
#
# print(data)


#2 variant                  # context manager   #PREFERABLE


# with open(filename, 'r') as my_file:
#     # data = my_file.read()
#     # data = my_file.readline()                 # построково
#     # for _ in range(6):
#     #     print(my_file.readline())
#     data = my_file.readlines()                  # список з строками
#
# print(data)
#
# data.append("\n\t\tteeeest9999999")
#
# with open(filename + "_test", 'w') as my_file:
#     # my_file.write(data)
#     my_file.writelines(data)
#
#
# print(data)


# def reading_text_file_readlines(file: str) -> list:
#     with open(file, 'r') as f:
#         data = f.readlines()
#     return data
#
#
# def writelines_text_file(file: str, data: list):
#     with open(file, 'w') as my_file:
#         my_file.writelines(data)
#
#
#
# data = reading_text_file_readlines(filename)
# print(data)


#How with(context manager) works

# try:
#     my_file = open(filename, 'r')     #'r' - read, 'w' - write
#     data = my_file.read()
# except:
#     print('error')
# finally:
#     my_file.close()






















################################### HW ######################################################
# persons = [{"name": "John", "age": 15},
#            {"name": "Anna", "age": 23},
#            {"name": "Dan", "age": 5},
#            {"name": "Maximus", "age": 24},
#            {"name": "Olgha", "age": 25},
#            {"name": "Volodymyr", "age": 5},
#            {"name": "Jack", "age": 45}]


# def exercise_4(persons_dict):
#     ages = []
#     names_lens = []
#     youngest_persons = []
#     long_name_persons = []
#
#     for person_dict in persons_dict:
#         ages.append(person_dict["age"])                             #put all age
#         names_lens.append(len(person_dict["name"]))                 #put all names
#
#     min_age = min(ages)
#     max_len_name = max(names_lens)
#
#     for person_dict in persons_dict:
#         if person_dict["age"] == min_age:
#             youngest_persons.append(person_dict["name"])
#
#     for person_dict in persons_dict:
#         if len(person_dict["name"]) == max_len_name:
#             long_name_persons.append(person_dict["name"])
#
#     average_age = sum(ages) / len(ages)
#
#     return [youngest_persons, long_name_persons, average_age]
#
#
# young_persons, longname_person, avrg_age = exercise_4(persons)
# print(young_persons, longname_person, avrg_age)



# ##########
my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
my_dict_2 = {11: 11, 2: 22}


def exercise_5(dict_1, dict_2):

    res_1 = list(set(dict_1.keys()).intersection(set(dict_2.keys())))

    res_2 = list(set(dict_1.keys()).difference(set(dict_2.keys())))

    res_3 = {key: dict_1[key] for key in result_2}

    res_4 = dict_1.copy()
    for key in dict_2:
        if key in result_4:
            result_4[key] = [result_4[key], dict_2[key]]
        else:
            result_4[key] = dict_2[key]

    return res_1, res_2, res_3, res_4


result_1, result_2, result_3, result_4 = exercise_5(my_dict_1, my_dict_2)
# print(exercise_5(my_dict_1, my_dict_2))
print(result_1)
print(result_2)
print(result_3)
print(result_4)