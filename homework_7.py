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

num = 26465000
num_str = str(num)
count_zeros = 0

for char in reversed(num_str):
    if char == '0':
        count_zeros += 1
    else:
        break

print(count_zeros)







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