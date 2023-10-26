# print("hello world")
my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
unique_chars_1 = []

for char in my_str_1: # символ в строке 1
    if my_str_1.count(char) == 1 and char not in unique_chars_1: # если нахождение символа в строке 1 = 1
        # и символа нет в уникальних символах
        unique_chars_1.append(char) #добавить символ в лист уникальние символи1


unique_chars_2 = []
for char in my_str_2:
    if my_str_2.count(char) == 1 and char not in unique_chars_2:
        unique_chars_2.append(char)


result = []


for char in unique_chars_1: # символ в уникаьних символах 1
    if char in unique_chars_2: # если символ в уникальних символах 2
        result.append(char) # добавь символ в результат

print(result)
