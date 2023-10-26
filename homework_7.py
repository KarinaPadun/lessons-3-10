# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.
num = 1230000046
num_1 = str(num)
count = num_1.count('0')
print(count)


# 1.2  Дано ціле число (int). Визначити скільки нулів у цьому числі.
num = 123000046
num_1 = str(num)
result = 0

for i in num_1:
    if i == '0':
        result += 1

print(result)

# 1.3  Дано ціле число (int). Визначити скільки нулів у цьому числі.

num = 123000046
num_2 = str(num)
result = 0
i = 0

while i < len(num_2):
    if num_2[i] == '0':
        result += 1
    i += 1

print(result)

#2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

num = 2640650000
num_str = str(num)
count_zeros = 0

for i in reversed(num_str):
    if i == '0':
        count_zeros += 1
    else:
        break

print(count_zeros)

# 2.1

num = 260465000
num_str = str(num)
result = 0

for i in num_str[::-1]:
    if i == '0':
     result += 1
    else:
        break
print(result)

# 3 Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

my_list_1 = [-3, 3, -455, 20, 114]
my_list_2 = [3, 0, 9, 4, 8, 11]
my_result = []


for i in my_list_1[::2]:
    my_result.append(i)

my_result.extend(my_list_2[::2])

print(my_result)

# 3.2

my_list_1 = [-3, 3, -455, 20, 114]
my_list_2 = [3, 0, 9, 4, 8, 11]
my_result = []

for i in my_list_1:
    if my_list_1.index(i) % 2 == 0:  #
        my_result.append(i)

for i in my_list_2:
    if my_list_2.index(i) % 2 == 0:
        my_result.append(i)

print(my_result)


# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

my_list = [2, 0, 3, 4]
new_list = []

for i in my_list:
    if my_list.index(i) != 0:
        new_list.append(i)

new_list.append(my_list[0])
print(new_list)

# 4.1

my_list = [2, 0, 3, 4]
new_list = []

for i in my_list[1:]:
    new_list.append(i)

new_list.append(my_list[0])

print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

my_list = [1, 2, 6, 5]

deleted_char = my_list.pop(0)
print(deleted_char)

my_list.append(deleted_char)

print(my_list)

