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
# my_result = [i for i in my_list_1[::2]]
# my_result.extend(my_list_2[::2])

my_result = []

for i in my_list_1[::2]:
    my_result.append(i)

my_result.extend(my_list_2[::2])

print(my_result)

# 3.2

my_list_1 = [-3, 3, -455, 20, 114]
my_list_2 = [3, 0, 9, 4, 8, 11]
my_result = []

# my_result = [my_list_1[i] for i in range(0, len(my_list_1), 2)] + [my_list_2[i] for i in range(0, len(my_list_2), 2)]

# my_result = [i for i in my_list_1[::2]] + [i for i in my_list_2[::2]]

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
#new_list = [i for i in my_list if my_list.index(i) != 0]
#new_list.append(my_list[0])

for i in my_list:
    if my_list.index(i) != 0:
        new_list.append(i)

new_list.append(my_list[0])
print(new_list)

# 4.1

my_list = [2, 0, 3, 4]
new_list = []
# new_list = [i for i in my_list[1:]]
# new_list.append(my_list[0])
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

# 5.2
my_list = [1, 2, 6, 5]

if my_list:
    first_char = my_list.pop(0)
    my_list.append(first_char)

print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)


my_string = 'Каті 15 років, її тату - 45'
words = my_string.split()
result = 0

for word in words:
    if word.isdigit():
        result += int(word)

print(result)
# 6. 1
my_string = 'Каті 15 років, мамі-38, тату - 45'
words = my_string.split()
numbers = []
num_str = ""

for word in words:
    for char in word:
        if char.isdigit():
            num_str += char
        elif num_str:
            numbers.append(int(num_str))
            num_str = ""


if num_str:
    numbers.append(int(num_str))

total_sum = sum(numbers)

print(numbers)
print(total_sum)

#7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
#які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
#Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
#Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
result_numbers = []

for i in range(1, len(my_list) - 1): # выдача от 1 символа до предпоследнего
    if my_list[i] > my_list[i - 1] + my_list[i + 1]:
        count += 1
        result_numbers.append(my_list[i])

print("Кількість елементів:", count)
print("Елементи, які більше суми сусідів:", result_numbers)


#8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
#Наприклад [1, 2, 3, "11", "22", 33]
#Створити новий список у який помістити лише рядки з my_list.

my_list = [1, 2, 3, "11", "22", 33]
new_list = []

for i in my_list:
    if type(i) != int:
        new_list.append(i)

print(new_list)

# 8.2

my_list = [1, 2, 3, "11", "22", 33]
new_list = []

for i in my_list:
    if type(i) == str:
        new_list.append(i)

print(new_list)

# 8.3
my_list = [1, 2, 3, "11", "22", 33]
new_list = [i for i in my_list if type(i) == str]

print(new_list)


# 9 Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

my_str = 'this is my home'
my_list = []

for i in my_str:
    if my_str.count(i) == 1:
        my_list.append(i)

print(my_list)

# 9.1

my_str = 'this is my home'
my_list = []
i = 0

while i < len(my_str):
    char = my_str[i]
    if my_str.count(char) == 1:
        my_list.append(char)
    i += 1

print(my_list)


# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

my_str = 'rtuff'
my_str_2 = 'ertyu'
result = []

for i in my_str:
    if i in my_str_2 and i not in result:
        result.append(i)

for i in my_str_2:
    if i in my_str and i not in result:
        result.append(i)

print(result)

# 10.2
my_str_1 = "abcde"
my_str_2 = "cdefg"

result = []

for char in my_str_1:
    if char in my_str_2:
        if my_str_1.count(char) == 1 and my_str_2.count(char) == 1:
            result.append(char)

print(result)


# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
new_list_1 = []

for i in my_str_1:
    if my_str_1.count(i) == 1 and i not in new_list_1:
        new_list_1.append(i)

new_list_2 = []
for i in my_str_2:
    if my_str_2.count(i) == 1 and i not in new_list_2:
        new_list_2.append(i)

result = []

for i in new_list_1:
    if i in new_list_2:
        result.append(i)

print(result)
