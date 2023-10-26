#print("hello world")
##Дано два рядка. Считайте список, в котором упоминаются те символы, которые находятся в обоих рядах, но в каждой ТИЛЬКЕ с одного раза.
#Пример: для рядов "aaaasdf1" и "asdfff2"
#повторения ["s", "d"], т.к. эти символы в каждом ряду по одному разу
my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
result = []

for i in my_str_1:
    if my_str_1.count(i) == 1 and i not in result:
        result.append(i)

for i in my_str_2:
    if my_str_2.count(i) == 1 and i not in result:
        result.append(i)

print(result)

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
result = []

for char in my_str_1:
    if my_str_1.count(char) == 1 and char not in my_str_2 and char not in result:
        result.append(char)

for char in my_str_2:
    if my_str_2.count(char) == 1 and char not in result:
        result.append(char)

print(result)




my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
unique_chars_1 = []

for char in my_str_1:
    if my_str_1.count(char) == 1 and char not in unique_chars_1:
        unique_chars_1.append(char)

# Створимо список для зберігання унікальних символів з другого рядка
unique_chars_2 = []
for char in my_str_2:
    if my_str_2.count(char) == 1 and char not in unique_chars_2:
        unique_chars_2.append(char)

# Створимо список для зберігання результатів
result = []

# Перевіримо, які символи є в обох списках унікальних символів
for char in unique_chars_1:
    if char in unique_chars_2:
        result.append(char)

print(result)
