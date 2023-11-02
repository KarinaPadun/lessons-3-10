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
    n_list = [j for j in list_2 if j.startswith('a')]
    return n_list


my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 2. 2


def new_list(list_2):
    n_list = [j for j in list_2 if j[0] == 'a']
    return n_list


my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.


def new_list(list_2):
    n_list = [j for j in list_2 if 'a' in j]
    return n_list


my_list = ['245', 'atyy', 'eta', 'ayu', 'ttie', '4743eda']
result = new_list(my_list)
print(result)


# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str)
# і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.


def new_list(list_2):
    n_list = [j for j in list_2 if type(j) == str]
    return n_list


my_list = [876, 'atyy', 567, 'ayu', 'ttie']
result = new_list(my_list)
print(result)

# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str,
# які зустрічаються у рядку лише один раз.


def new_str(string):
    n_str = [item for item in set(string) if my_str.count(item) == 1]
    return n_str


my_str = 'ryttyyte'
result = new_str(my_str)
print(result)

# 5. 2


def new_str(string):
    n_str = [j for j in set(string) if my_str.count(j) < 2]
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

def unique_symbols(str1, str2):
    my_symbols = [char for char in set(str1) if char in str2]
    return my_symbols


string_1 = 'qwertyy'
string_2 = 'qwedfgh'
result = unique_symbols(string_1, string_2)
print(result)


# 6.2
def unique_symbols(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    my_symbols = list(set1.intersection(set2))
    return my_symbols


string_1 = 'qwertyy'
string_2 = 'qwedfgh'
result = unique_symbols(string_1, string_2)
print(result)


# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
def unique_symbols(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    my_symbols = [symbol for symbol in set1.intersection(set2) if string_1.count(symbol) + string_2.count(symbol) == 2]
    return my_symbols


string_1 = 'Helloy'
string_2 = 'Goodbye'
result = unique_symbols(string_1, string_2)
print(result)


# 7.2
def unique_characters(str1, str2):
    unique_chars = []

    for char in str1:
        if char in str2 and str1.count(char) == 1 and str2.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)

    for char in str2:
        if char in str1 and str2.count(char) == 1 and str1.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)

    return unique_chars


string_1 = 'Helloy'
string_2 = 'Goodbye'
result = unique_characters(string_1, string_2)
print(result)
