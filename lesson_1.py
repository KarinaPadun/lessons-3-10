#print("hello world")

my_string = 'Каті 15 років, мамі - 38, тату - 45'
words = my_string.split()

numbers = []  # Створюємо список для збереження чисел

for word in words:
    for char in word:
        if char.isdigit():
            numbers.append(int(char))  # Додаємо число до списку чисел

print(numbers)

my_string = 'Каті 15 років, мамі - 38, тату - 45'
words = my_string.split()
numbers = []

for word in words:
    num_str = ''
    for char in word:
        if char.isdigit():
            num_str += char
        elif num_str:
            numbers.append(int(num_str))
            num_str = ''


if num_str:
    numbers.append(int(num_str))

total_sum = sum(numbers)  # Обчислюємо суму чисел
print(total_sum)  # Результат: 98


my_string = 'Каті - 15 років, мамі - 37, тату - 45'
words = my_string.split()

numbers = []  # Створюємо список для збереження чисел

for word in words:
    num_str = ""
    for char in word:
        if char.isdigit():
            num_str += char
        elif num_str:
            numbers.append(int(num_str))
            num_str = ""

# Перевіряємо, чи є останній символ числовим
if num_str:
    numbers.append(int(num_str))

total_sum = sum(numbers)  # Обчислюємо суму чисел

print(numbers)
print(total_sum)

