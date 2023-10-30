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




#4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
#а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
#б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
#в) Порахувати середню вік усіх людей із початкового списку.

#5) Дано два словники my_dict_1 і my_dict_2.
#а) Створити список із ключів, які є в обох словниках.
#б) Створити список із ключів, які є у першому, але немає у другому словнику.
#в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
#г) Об'єднати ці два словники у новий словник за правилом:
#якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
#якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

#{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}