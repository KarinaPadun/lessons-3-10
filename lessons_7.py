# Ви маєте змінну my_str, тип - str. Надрукувати ЧИСЛО скільки РІЗНИХ символів зустрічається в my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str="bla BLA car"
#            Виведення на екран: 6


# 1
# .lower()
# val_list = []
# for + if statement

# my_str = "bla BLA car"
# unique_chars = []
#
# for char in my_str.lower():
#     if char not in unique_chars:
#         unique_chars.append(char)
#
# count_unique_chars = len(unique_chars)
#
# print(count_unique_chars)

# my_str = "bla BLA car"
# my_list = []
#
# temp_list = list(my_str.lower())
# # print(temp_list)
# for i in temp_list:
#     if i not in my_list:
#         my_list.append(i)
#
# print(len(my_list))

# 2
# my_str = "bla BLA car".lower()
#
# temp_list = list(my_str.lower())
#
# my_list = []
# count = 0

# while len(temp_list) != 0:
# while len(temp_list):
# while temp_list:
# while count < len(temp_list):
# while count < len(my_str):
#     if my_str[count] not in my_list:
#     # if temp_list[count] not in my_list:
#         my_list.append(my_str[count])
#
#     count += 1
#
#     # symb = temp_list.pop()
#     #
#     # if symb not in my_list:
#     #     my_list.append(symb)
#
# print(len(my_list))


################################################
# Ви маєте змінну my_str, та порожній список my_list. Заповнити my_list УНІКАЛЬНИМИ символами з my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "l", "a", " ", "c", "r"]

# my_str = "bla BLA car"
# my_list = []
#
# for char in my_str.lower():
#     if char not in my_list:
#         my_list.append(char)
#
# print(my_list)

################################################
# Дано рядок my_str та порожній список my_list. Заповнити my_list символами з my_str,
# які стоять на парних місцях у рядку (рахуэмо з 0)
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "a", "B", "A", "c", "r"]

# my_str = "bla BLA car"
# my_list = []
# for with index of str


#1
# my_list += list(my_str[::2])

# my_list.append((list(my_str[::2]))) # ліст в лісті


#2
# for symb in my_str[::2]:
#     my_list.append(symb)

#3
# for i in range(0, len(my_str), 2):
#     my_list.append(my_str[i])

#4
# for i in range(len(my_str)):
#     if not i % 2:
#         my_list.append(my_str[i])


################################################
# Дано рядок my_str, список str_index цілих чисел в діапазоні від 0 до довжини рядка мінус 1,
# пустий список my_list. Заповнити my_list символами my_str, які стоять на місцях з
# індексами із str_index
# Наприклад: key = "bla BLA car"
#            str_indexes = [0, 2, 4, 4, 8]
#            Виведення на екран: ["b", "a", "B", "B", "c"]

# key = "bla BLA car"
# str_indexes = [0, 2, 4, 4, 8]
# my_list = []

# for index in str_indexes:
#     if 0 <= index < len(key):
#         my_list.append(key[index])
#
# print(my_list)

# for index in str_indexes:
#     if index < len(key):
#         my_list.append(key[index])
#
# print(my_list)

################################################
# Дано ціле число (int). Визначити скільки цифр у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 6

# my_number = 228989

# num_str = str(my_number)
# numbers_of_units = len(num_str)
# print(numbers_of_units)

# print(len(str(my_number)))

# Дано ціле число. Визначити найбільшу цифру у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 9

# my_number = str(228989)
# check_num = 9
#
# while True:
#     if str(check_num) in my_number:
#         break
#     check_num -= 1
#
# print(check_num)

# maximum = max(str(my_number))
# minimum = min(str(my_number))
# print(maximum)

# Дано ціле число. Скласти число (int) із цифрами у зворотному порядку.
# Наприклад: my_number = 1263
#            Виведення на екран: 3621

# my_number = 1263
#
# print(str(my_number)[::-1])

# Дано ціле число. Скласти число з цифрами в порядку зростання (зменшення).
# Наприклад: my_number = 3254
#            Виведення на екран: 2345   #зростання
#            Виведення на екран: 5432   #зменшення

# my_number = 3254

# sorted_number = ''.join(sorted(str(my_number)))
# result = int(sorted_number)
# print(result)

# number_incr = "".join(sorted(str(my_number)))
# number_decr = "".join(sorted(str(number), reverse=True))

################################################
# Дано списки my_list_1 та my_list_2. Створити список my_result в який помістити елементи
# з my_list_1 та my_list_2 через один, починаючи з my_list_1.
# a) кількість ел-тів однакове
# б) кількість ел-тів різне
# Наприклад: my_list_1 = [1, 2, 3]
#            my_list_2 = [10, 20, 30] # для варінту a
#            my_list_2 = [10, 20, 30, 40] # для варінту б
#            Виведення на екран: [1, 10, 2, 20, 3, 30]   #ел-тів однакове
#            Виведення на екран: [1, 10, 2, 20, 3, 30, 40]   #ел-тів різне
#
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
#
# for i in range(len(my_list_1)):
#     my_result.append(my_list_1[i])
#     my_result.append(my_list_2[i])
#
# print(my_result)

# my_list_1 = [1, 2, 3, 4, 5, 6, 99, 101]
# my_list_2 = [8, 9, 10, 11, 12]
# my_result = []
#
# i = 0
# #
# min_length = min(len(my_list_1), len(my_list_2))
#
# # for i in min_length:
# while i < min_length:
#     my_result.append(my_list_1[i])
#     my_result.append(my_list_2[i])
#     i += 1
#
# my_result += my_list_1[i:]
# my_result += my_list_2[i:]
#
# my_result.extend(my_list_1[i:])
# my_result.extend(my_list_2[i:])
#
# print(my_result)
