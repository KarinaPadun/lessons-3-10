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
for char in my_str:
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