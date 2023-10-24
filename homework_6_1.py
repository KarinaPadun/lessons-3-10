#Ви маєте змінну my_str, тип - str. Надрукувати ЧИСЛО скільки РІЗНИХ символів зустрічається в my_str.
#Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
#Наприклад: my_str="bla BLA car"

my_str = "Twelve, minutes"
unique_chars = set(my_str.lower())  # Перетворення усіх літер в нижній регістр та використання множини для визначення унікальних символів
count_unique_chars = len(unique_chars)  # Підрахунок кількості унікальних символів

print(count_unique_chars)

# Класс set (множество) — это одна из ключевых структур данных в Python.
# Она представляет собой неупорядоченную коллекцию уникальных элементов.
# в некоторой степени, соответствует математическому множеству.


my_str = "Ttt Oop  "
unique_chars = []
for char in my_str.lower:
    if char not in unique_chars:
        unique_chars.append(char)

count_unique_chars = len(unique_chars)

print(count_unique_chars)



#Ви маєте змінну my_str, та порожній список my_list. Заповнити my_list УНІКАЛЬНИМИ символами з my_str.
#Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
#Наприклад: my_str = "bla BLA car"
#           Виведення на екран: ["b", "l", "a", " ", "c", "r"]

my_str = 'I am 12 years old '
my_list = []

my_str = my_str.lower()

for char in my_str:
    if char not in my_list:
        my_list.append(char)

print(my_list)
############################
my_str = 'I am 12 years '
my_list = []
my_str = my_str.lower()

my_list = list(set(my_str))

print(my_list)
#####################
#Дано рядок my_str та порожній список my_list. Заповнити my_list символами з my_str,
#які стоять на парних місцях у рядку (вважаємо з 0)
#Наприклад: my_str = "bla BLA car"
           #Виведення на екран: ["b", "a", "B", "A", "c", "r"]
my_str = 'hi! how are you'
my_list = []

for i in range(0, len(my_str), 2):
    my_list.append(my_str[i])

print(my_list)
####################################
my_str = 'hi! how are you'
my_list = list(my_str[::2])

print(my_list)

#########################################
#Дано рядок my_str, список str_index цілих чисел в діапазоні від 0 до довжини рядка мінус 1, пустий список my_list.
#Заповнити my_list символами my_str, які стоять на місцях з індексами із str_index
my_str = 'eiri eir fvvf g '
str_index= [1, 3, 5, 6, 8, 12]
my_list = []

for index in str_index:
    if 0 <= index < len(my_str): #проверяет находятся индексы в строке или нет
        my_list.append(my_str[index])

print(my_list)



# Дано ціле число (int). Визначити скільки цифр у цьому числі.
#Наприклад: my_number = 228989
#          Виведення на екран: 6
value = '456993846'
print(len(value))

#Дано ціле число. Визначити найбільшу цифру у цьому числі.
#Наприклад: my_number = 228989
       #    Виведення на екран: 9
value = '456003846'



value_str = str(value)

max_digit = 0


for digit_str in value_str:
    digit = int(digit_str)
    if digit > max_digit:
        max_digit = digit

print(f"Найбільша цифра у числі {value_str} - це {max_digit}.")


value_1 = '99664210'


value_1_str = str(value_1)


max_digit = max(value_1, key=int) #Функция max возвращает максимальное число из группы чисел, заданных в параметрах

print(f"Найбільша цифра у числі {value_1} - це {max_digit}.")


#Дано ціле число. Скласти число (int) із цифрами у зворотному порядку.
#Наприклад: my_number = 123
#          Виведення на екран: 321
my_number = '45678'

print(my_number[::-1])
########################################
my_number = '45678901'

reversed_str = my_number[::-1]

reversed_number = int(reversed_str)

print(reversed_number)


#Дано ціле число. Скласти число з цифрами в порядку зростання (зменшення).
# зростання
number = '6758438'


sorted_number = ''.join(sorted(number))

result = int(sorted_number)

print(result)


# зменшення
number = '13580'


sorted_number = ''.join(sorted(number, reverse=True))


result = int(sorted_number)

print(result)




#Дано списки my_list_1 та my_list_2. Створити список my_result в який помістити елементи
#з my_list_1 та my_list_2 через один, починаючи з my_list_1.
#a) кількість ел-тів однакове

my_list_1 = [1,2,3,4,5,6]
my_list_2= [7,8,9,10,11,12]
my_result = []

for i in range(len(my_list_1)):
    my_result.append(my_list_1[i])
    my_result.append(my_list_2[i])

print(my_result)
#2 v?
my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [6, 8, 9, 10, 11, 12]


my_result = [item for pair in zip(my_list_1, my_list_2) for item in pair] # zip только к словарям?

print(my_result)


#б) кількість ел-тів різне

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_2 = [8, 9, 10, 11, 12]
my_result = []

min_length = min(len(my_list_1), len(my_list_2))

for i in range(min_length):
    my_result.append(my_list_1[i])
    my_result.append(my_list_2[i])

# Додаємо залишок елементів, якщо вони є
my_result.extend(my_list_1[min_length:])
my_result.extend(my_list_2[min_length:])

print(my_result)

#############################################

my_list_1 = [1, 2, 3, 4, 5, 6, 99, 101]
my_list_2 = [8, 9, 10, 11, 12]
my_result = []

i = 0
while i < min(len(my_list_1), len(my_list_2)):
    my_result.append(my_list_1[i])
    my_result.append(my_list_2[i])
    i += 1

#   добавляем остаток , если он есть extend - в конец списка
my_result.extend(my_list_1[i:])
my_result.extend(my_list_2[i:])

print(my_result)


