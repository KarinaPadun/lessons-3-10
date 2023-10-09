# data types

#int - intenger ціле число , незмінна
#float - дробні числа , незмінна
#complex (2+5c), незмінна
#decimal - більш точні 2.99999999, межа набато далі , ніж в дробних

#string - строка, незмінна
#str


#None - пуста множина, незмінний


#bolean bool (True/ False) логічний оператор , змінний

#tuple - кортежи (незмінні) ()

#змінні:
#list - список []
#set - множина {}
#dict - словник зберігає в парі ( key: Value), змінний



box = 1
new_box = box

box = 2

print(new_box, type(new_box), id(new_box))

# id() - показує адресу файлу
# type() - показує тип файлу

# constants - Дані , які не треба змінювати, з великої літери

PI = 3,14

###################################################################

num_1 = 2
num_2 = 10

result_add = num_1 + num_2
result_sub = num_1 - num_2
result_mul = num_1 * num_2
result_div = num_1 / num_2
result_div_2 = num_1 // num_2  # цілочисленне ділення
result_div_3 = num_1 % num_2 # залишок ділення
result_power = num_1 ** num_2 # зведення в ступінь
result_root = num_1 ** 0,5  # корінь від числа

######################################################################

# string

some_text1 = "Hello \nI\'m Nick "
some_text = 'Hello'
some_text = """Hello"""
some_text = '''Hello'''

print(some_text1)




