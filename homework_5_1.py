#1) У вас є рядок my_string = '0123456789'.
#Згенерувати цілі числа (тип int) від 0 до 99 та роздрукувати їх.
#Завдання потрібно виконати через цикл у циклі (див. приклад нижче) та наведення типів.
#Генерування через range або інші "фішки" можна в якості альтернативного вирішення, але спершу через цикл у циклі))


my_string = '0123456789'

for i in range(10):
    for j in range(10):
        num_str = my_string[i] + my_string[j]
        num_int = int(num_str)
        print(num_int)

#2
my_string = '0123456789'

for tens_digit in my_string:
    for ones_digit in my_string:
        number_str = tens_digit + ones_digit
        number_int = int(number_str)
        print(number_int)

string = '0123456789'

tens_digit = 0  # дві змінні відповідають за індекси для чисел
while tens_digit < 10:
    ones_digit = 0 # став 1
    while ones_digit < 10:
        num_str = string[tens_digit] + string[ones_digit] # 0 + 0 - 0 +1
        num_int = int(num_str) # 00- 0 , 01- 1
        print(num_int)
        ones_digit += 1
    tens_digit += 1

my_string = '0123456789'

number = 0
while number < 100:
    print(number)
    number += 1

my_string = '0123456789'

number = 0
while number < 100:
    num_str = my_string[number // 10] + my_string[number % 10]
    num_int = int(num_str)
    print(num_int)
    number += 1
