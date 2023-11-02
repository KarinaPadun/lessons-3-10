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
    n_list = [i[::-1] if index % 2 == 1 else i for index, i in enumerate(list_1)]
    return n_list


my_list = ['245', '567', '3578', '5645', '7564']
result = new_list(my_list)
print(result)


# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".
def new_list(list_2):
    n_list = [i for i in list_2 if i.startswith('a')]
    return n_list


my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 2. 2


def new_list(list_2):
    n_list = [i for i in list_2 if i[0] == 'a']
    return n_list


my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.


def new_list(list_2):
    n_list = [i for i in list_2 if 'a' in i]
    return n_list


my_list = ['245', 'atyy', 'eta', 'ayu', 'ttie', '4743eda']
result = new_list(my_list)
print(result)


# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str)
# і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.


def new_list(list_2):
    n_list = [i for i in list_2 if type(i) == str]
    return n_list


my_list = [876, 'atyy', 567, 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str,
# які зустрічаються у рядку лише один раз.


def new_str(string):
    n_str = [i for i in set(my_str) if my_str.count(i) == 1]
    return n_str


my_str = 'ryttyyte'
result = new_str(my_str)
print(result)

# 5. 2


def new_str(string):
    n_str = [i for i in set(string) if my_str.count(i) < 2]
    return n_str


my_str = 'ryttyyte'
result = new_str(my_str)
print(result)

# 5. 3


def unique_characters(string):
    char_count = {}
    unique_chars = []

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)

    return unique_chars


my_str = "abrabrtyu"
result = unique_characters(my_str)
print(result)



# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.




# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.