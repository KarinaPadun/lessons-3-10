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

# 2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
# які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for.

my_list = [0, 1 , 999, 2020, 20, 102, 101, -3]
my_results = []

for i in my_list:
    if i > 100:
     my_results.append(i)


print(my_results)

