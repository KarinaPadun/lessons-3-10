# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

my_list = ['245', 'rtyy', 'et', 'yyu', 'ttie']
my_result = []

for index, i in enumerate(my_list):
    if index % 2 == 1:
        my_result.append(i[::-1])
    else:
        my_result.append(i)

print(my_result)

# 1.2
my_list = ['245', 'rtyy', 'et', 'yyu', 'ttie']
my_result = [i[::-1] if index % 2 == 1 else i for index, i in enumerate(my_list)]

print(my_result)

# 1.3
my_list = ['245', '567', '3578', '5645', '7564']
my_result = []

for index, string in enumerate(my_list):
    if index % 2 == 1:
        reversed_string = string[::-1]
        my_result.append(reversed_string)
    else:
        my_result.append(string)

print(my_result)
# 1. 4
my_list = ['245', '567', '3578', '5645', '7564']
my_result = []

for i in range(len(my_list)):
    if i % 2 == 1:
        reversed_string = my_list[i][::-1]
        my_result.append(reversed_string)
    else:
        my_result.append(my_list[i])

print(my_result)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".
my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
my_result = [i for i in my_list if i.startswith('a')]
print(my_result)

# 2.1
my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
my_result = []

for i in my_list:
    if i[0] == 'a':
        my_result.append(i)

print(my_result)
# 2 .2
my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
my_result = [i for i in my_list if i[0] == 'a']
print(my_result)

# 2 .3
my_list = ['245', 'atyy', 'et', 'ayu', 'ttie']
my_result = []

for i in range(len(my_list)):
    if my_list[i][0] == 'a':
        my_result.append(my_list[i])

print(my_result)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

my_list = ['245', 'atyy', 'eta', 'ayu', 'ttae']
my_result = []

for i in my_list:
    if 'a' in i:
        my_result.append(i)

print(my_result)

# 3 . 2

my_list = ['245', 'atyy', 'eta', 'ayu', 'ttae']
my_result = [i for i in my_list if 'a' in i]

print(my_result)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# в) Порахувати середню вік усіх людей із початкового списку.

# 4 а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
value_dict = [{
    "name": "John",
    "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Lora",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

min_age = min(i["age"] for i in value_dict)

my_list = [i for i in value_dict if i["age"] == min_age]

print(my_list)

# 4.2 а)

value_dict = [{
    "name": "John",
    "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Lora",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

min_age = min(i["age"] for i in value_dict)

my_list = []

for i in value_dict:
    if i["age"] == min_age:
        my_list.append(i)

print(my_list)

# 4.3 а)
value_dict = [
    {"name": "John",
     "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Lora",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

min_age = min(i["age"] for i in value_dict)
my_list = []

i = 0
while i < len(value_dict):
    if value_dict[i]["age"] == min_age:
        my_list.append(value_dict[i])
    i += 1

print(my_list)


# 4 б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.

value_dict = [{
    "name": "John",
    "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Lora",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

max_name = max(len(i["name"]) for i in value_dict)

my_list = []

for i in value_dict:
    if len(i["name"]) == max_name:
        my_list.append(i)

print(my_list)

# 4.2 б)
value_dict = [{
    "name": "John",
    "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Maksi",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

max_name = max(len(i["name"]) for i in value_dict)

my_list = [i for i in value_dict if len(i["name"]) == max_name]

print(my_list)

# 4.3  б)
value_dict = [
    {"name": "John",
     "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Makcs",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]
my_list = []
max_name_length = max(len(i["name"]) for i in value_dict)

i = 0
while i < len(value_dict):
    if len(value_dict[i]["name"]) == max_name_length:
        my_list.append(value_dict[i])
    i += 1

print(my_list)

# 4 в) Порахувати середню вік усіх людей із початкового списку.
value_dict = [
    {"name": "John",
     "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Makcs",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

ages = [i["age"] for i in value_dict]

print(ages)

result = sum(ages) / len(ages)

print(result)

# 4.2  в)

value_dict = [
    {"name": "John",
     "age": 15},
    {"name": "Emily",
     "age": 12},
    {"name": "Makcs",
     "age": 12},
    {"name": "Jack",
     "age": 45},
    {"name": "Den",
     "age": 35}
]

result = sum([i["age"] for i in value_dict]) / len([i["age"] for i in value_dict])

print(result)

# 5) Дано два словники my_dict_1 і my_dict_2.
# а) Створити список із ключів, які є в обох словниках.
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# 5 а) Створити список із ключів, які є в обох словниках.

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

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

result = keys_1.intersection(keys_2)
# result = list(keys_1.intersection(keys_2)) -другий вариант
print(result)

# 5.2  а)

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
my_result = []

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

for key in keys_1:
    if key in keys_2:
        my_result.append(key)

print(my_result)

# 5.3  а)
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

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

my_result = [key for key in keys_1 if key in keys_2]

print(my_result)

# 5 б) Створити список із ключів, які є у першому, але немає у другому словнику.
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
my_result = []

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

for key in keys_1:
    if not key in keys_2:
        my_result.append(key)

print(my_result)

# 5. 2 б) Створити список із ключів, які є у першому, але немає у другому словнику.

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

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

my_result = [key for key in keys_1 if key not in keys_2]
print(my_result)

# 5 в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
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
keys_2 = {list(i.keys())[0] for i in my_dict_2}

for i in my_dict_1:
    for key in i:
        if key not in keys_2:
            my_new_dict[key] = i[key]

print(my_new_dict)

# 5.2 в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
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

keys_2 = {list(i.keys())[0] for i in my_dict_2}

my_new_dict = [{key: i[key] for i in my_dict_1 for key in i if key not in keys_2}]

print(my_new_dict)


# 5 г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}


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

keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

for key in keys_1:
    if key in keys_2:
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i] + [i[key] for i in my_dict_2 if key in i]
    else:
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i][0]

print(my_new_dict)

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

for key in my_dict_1:
    if key not in my_dict_2:
        my_new_dict[key] = my_dict_1[key]

for key in my_dict_2:
    if key not in my_dict_1:
        my_new_dict[key] = my_dict_2[key]

for key in my_dict_1:
    if key in my_dict_2:
        my_new_dict[key] = [my_dict_1[key], my_dict_2[key]]
print(my_new_dict)

