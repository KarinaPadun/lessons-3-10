# list comprehension
# sets
# sets methods(union(), difference(), intersection())

# list = []
# list += (my_str [::2])   # щоб лист не перестворювався , поставити +=
################# list comprehension
value_str = [1, 2, 3, 4]
# some_list = []
# for i in value_str:
#     if not (i**2) % 2:
#         some_list.append(i**2)

# some_list = [i for i in value_str]
# some_list = [i**2 for i in value_str]
# some_list = [i**2 for i in value_str if not (i**2) % 2]

# print(some_list)

# list comprehension - генератор списків . генерує списки та кладе туди елементи

################ sets
# sets - множина , не має послідовності, зміняємий тип данних як і ліст

# value_list = [1, 2, 2, 3, 24, 34, 9]
# print(value_list)
# value_set = set(value_list) - прінт унікальних значень у фігурних скобках , інт - порядок один

# print(value_set)

# value_list = ["1", "2", "2", "3", "4", "4", "9"] - порядок видачі буде відрізнятися постійно

#  інти розкладає в певному порядку , бо зазделегідь знає що буде з ними працювати.

####### sets methods(union(), difference(), intersection())

# Command + Option + L (mac)/ Ctrl + Alt + L (Win) - відрегувати по пеп 8, вирівняє

# value_set_1 = {1, 2, 3, 4, 5, 30}
# value_set_2 = {10, 2, 30}
# value_set_1 = value_set_1.union(value_set_2) # "+"

# union() - обєднання

# print(value_set_1)

# new_set_1 = value_set_1.difference(value_set_2) - убирает совпадение
# difference() ВАЖЛИВИЙ ПОРЯДОК
#
# new_set = value_set_2.difference(value_set_1)"-" ПОРЯДОК ЗАПИСУ ВАЖЛИВИЙ


# value_set_1 = value_set_1.intersection(value_set_2) # перехрещення/порівняння (те що є в обидвох сетах)


# value_set_1 = value_set_1.union(value_set_2) # "+"
# new_set_1 = value_set_1.difference(value_set_2)
# print(new_set_1)
#
# new_set = value_set_2.difference(value_set_1)
# print(new_set)
# #
# new_set_2 = new_set_1.union(new_set) # "-" ПОРЯДОК ЗАПИСУ ВАЖЛИВИЙ
# print(new_set_2)