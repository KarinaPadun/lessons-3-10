# 1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100. Завдання виконати за допомогою циклу for.

my_list = [1, 99, 102, 105, 2001, 999]
for i in my_list:
    if i > 100:
     print(i)

# 1.2 варіант
my_list = [1, 99, 102, 105, 2001, 999]

for i in range(len(my_list)):
    if my_list[i] > 100:
        print(my_list[i])

