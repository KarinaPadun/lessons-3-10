# print("hello world")

# 5.2  г) Об'єднати ці два словники у новий словник за правилом:

my_dict_1 = {
    "name": "John",
    "pets": "cat",
    "city": "New York",
    "work": "office"
}

my_dict_2 = {
    "name": "Jonn",
    "age": 43,
    "family": "mom and dad",
    "work": "shop assistant"
}

my_new_dict = {}

for key in my_dict_1: # ключ в моем словаре один
    if key not in my_dict_2: # если ключа нет в моем словаре 2
        my_new_dict[key] = my_dict_1[key] # добавляю в мой новий словарь ключ + значение
print(my_new_dict)
for key in my_dict_2: # ключ в моем словаре два
    if key not in my_dict_1: # если ключа нет в моем словаре 1
        my_new_dict[key] = my_dict_2[key] # добавляю в мой новий словарь ключ + значение
print(my_new_dict)
for key in my_dict_1: # ключ в моем словаре один
    if key in my_dict_2: # если ключ есть в моем словаре 2
        my_new_dict[key] = [my_dict_1[key], my_dict_2[key]] # добавляю в мой новий словарь ключ + значение из словаря один+значение из словаря два

print(my_new_dict)

# первій вариант
my_dict_1 = [
    {"name": "John"},
    {"pets": "cat"},
    {"city": "New York"},
    {"work": "office"}
]

my_dict_2 = [
    {"name": "Jonn"},
    {"age": 43},
    {"family": "mom and dad"},
    {"work": "shop assistant"}
]

my_new_dict = {}

keys_1 = {list(i.keys())[0] for i in my_dict_1} # собираю в лист ключи из словаря один
keys_2 = {list(i.keys())[0] for i in my_dict_2} # собираю в лист ключи из словаря два

for key in keys_1: # ключ из ключей один
    if key in keys_2: # если ключ есть в ключах два
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i] + [i[key] for i in my_dict_2 if key in i]
    # мой новий словарь(ключ)  = переменная ключа из словаря один если ключ есть в переменной
    # плюс переменная ключа из словаря два если ключ есть в переменной
    else: # в другом случае
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i][0] # мой новий словарь ключ = переменная ключа из словаря 1
        # если ключ есть в переменной

print(my_new_dict)




my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']

my_result = [i for i in my_list if i.startswith('a')]
print(my_result)

