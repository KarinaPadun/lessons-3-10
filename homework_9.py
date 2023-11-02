# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.
def new_list(list_1):
    n_list = [i if list_1.index(i) % 2 == 0 else i[::-1] for i in list_1]
    return n_list


my_list = ['245', 'rtyy', 'et', 'yyu', 'ttie']
result = new_list(my_list)
print(result)

# 1.2


def new_list(list_1):
    n_list = [i for i in range(len(my_list)) if i % 2 == 1 else i]
    return n_list


my_list = ['245', '567', '3578', '5645', '7564']
result = new_list(my_list)
print(result)




# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".


def new_list(my_list):
    new_list = [i for i in my_list if i.startswith('a')]
    return new_list


my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
result = new_list(my_list)
print(result)






# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.





# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.


#5. Написати функцію яка приймає один параметр – рядок my_str.
#Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.

#6. Написати функцію яка приймає один параметр - два рядки.
#Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

#7. Написати функцію яка приймає два параметри - два рядки.
#Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.