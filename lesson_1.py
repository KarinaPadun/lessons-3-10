#print("hello world")



my_string = 'Каті 15 років, мамі - 38, тату - 45'
words = my_string.split()

numbers = []  # Створюємо список для збереження чисел

for word in words:
    for char in word:
        if char.isdigit():
            numbers.append(int(char))  # Додаємо число до списку чисел

print(numbers)

numbers_1 = numbers.join(i[0],i[1])


