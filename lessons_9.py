# moduls
# def
# rstrip - кінець - початок, strip - початок убирает пробели
# += - добавит єлемент , арренд - добавляет цельний обьект

########### HW ############

# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.


def count_symb(obj, symb):

    num_str = str(obj)
    result = num_str.count(symb)

    return result


num = 100500
find_symbol = "0"
result = count_symb(num, find_symbol)
# result = count_symb(100500, "0")
print(result)


# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# num = 100500
# find_symbol = "0"
#
# new_list = []
# result = 0
#
# for symbol in str(num)[::-1]:
#     if symbol == find_symbol:
#         result += 1
#         new_list.append(symbol)
#     else:
#         break
#
# print(new_list, len(new_list))
# print(result)

# # strip() rstrip()
# first_name = " Nick     "
# print(first_name, len(first_name))
# print(first_name.strip(), len(first_name.strip()))


# num_str = str(num)
# result = (len(num_str) - len(num_str.rstrip(find_symbol)))
# print(result)
#
#
# val_str = str(num)[::-1] #005001
# without_zero = int(val_str)
# result = (len(str(num)) - len(str(without_zero)))
# print(result)


# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = ["q", "w", "e", "r", "t", "y"]
# my_list_2 = ["1", "2", "3", "4", "5", "6"]
#
# my_result = my_list_1[::2] + my_list_2[::2]
# print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

my_list = [[1,2,3], "23", "3", "4"]


def adding_last_obj_to_list(obj_list):
    obj_list.append(obj_list.pop(0))
    return obj_list


# new_list = adding_last_obj_to_list(my_list).copy()
# new_list = adding_last_obj_to_list(my_list)

# print(new_list, id(my_list), id(new_list))


# my_list = [[1,2,3], "23", "3", "4"]
#
# new_list = my_list[1:] + [my_list[0]]
# # new_list = ["hello", "end"]
# # new_list += my_list[1]
#
# new_list = my_list[1:]
# new_list.append(my_list[0])
#
# print(new_list)

#
# # 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# # [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
#
# my_list = ["one", "two", "tree", "four"]
# my_list.append(my_list.pop(0))
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)
#
# test_str = "43 більше ніж 34y8yyyy8 але менше ніж 56"
# numb_list = []

# string = "45, 67| is an-awesome 78! website"
# delimiters = [",", "|", ";", "!"]
# for delimiter in delimiters:
#     string = " ".join(string.split(delimiter))

# result = string.split()
#
# for i in test_str:
#     if not i.isdigit():
#         test_str = test_str.replace(i, " ")
# numb_list = test_str.split()
#
# print(sum(numb_list))
#
# my_list = test_str.replace(",", " ").split(" ")
#
# for word in test_str.split():
#     if word.isdigit():
#         numb_list.append(int(word))
#     else:
#         digit = ""
#         for symbol in word:
#             if symbol.isdigit():
#                 digit += symbol
#             else:
#                 if digit:
#                     numb_list.append(int(digit))
#                 digit = ""
#
#
# result = sum(numb_list)
# print(result, numb_list)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 1]
# result = 0
#
# for index in range(1, len(my_list)-1):
#     if my_list[index] > my_list[index - 1] + my_list[index + 1]:
#         result += 1
#
# print(result)

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
#
# for value in my_list:
#     if type(value) == str:  #isinstance(value, str)
#         new_list.append(value)
#
# print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = "hrrrrrrhhhauuuub"
# res_list = []
#
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         res_list.append(symbol)
#
# print(res_list)

# my_str = "gygygpo"
# new = []
# for i in set(my_str):
#     if my_str.count(i) < 2:
#         new.append(i)
# print(new)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
#
# my_set = set(my_str_1).intersection(set(my_str_2))
# res_list = list(my_set)
# print(res_list)


# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ один раз.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу
#
# my_str_1 = "aaaasd1ekoko212"
# my_str_2 = "asdff2"
# res_list = []
#
# for symbol in set(my_str_1).intersection(set(my_str_2)):
#     if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
#     # if my_str_1.count(symbol) + my_str_2.count(symbol) == 2:
#         res_list.append(symbol)
#
# print(res_list)

# val_str = ""
#
# for i in set():
#     val_str += str(i)