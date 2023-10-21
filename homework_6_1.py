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
