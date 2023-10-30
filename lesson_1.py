# print("hello world")

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

# Запитуємо всі унікальні ключі з обох словників
keys_1 = {list(i.keys())[0] for i in my_dict_1}
keys_2 = {list(i.keys())[0] for i in my_dict_2}

# Перевіряємо ключі і об'єднуємо словники
for key in keys_1:
    if key in keys_2:
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i] + [i[key] for i in my_dict_2 if key in i]
    else:
        my_new_dict[key] = [i[key] for i in my_dict_1 if key in i][0]

print(my_new_dict)
