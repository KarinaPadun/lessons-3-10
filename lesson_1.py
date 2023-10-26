#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])
my_string = 'Каті 12 років, її тату 45, а мамі 37'
words = my_string.split()
total_sum = 0

for word in words:
    if word.isdigit():
        total_sum += int(word)

print(total_sum)  # Результат: 94

my_list = [1, 2, 3, "11", "22", 33]
new_list = []

for i in my_list:
    if not isinstance(i, int):
        new_list.append(i)

print(new_list)
