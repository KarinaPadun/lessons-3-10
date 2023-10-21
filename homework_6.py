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

# 2.2 варіант

my_list = [0, 1 , 999, 2020, 20, 102, 101, -3]
my_results = [i for i in my_list if i > 100] # мой результат = і если i > 100 в my_list, цикл for перебирает значения в списке
print(my_results)

# 3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
# то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
# то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)

my_list = [-5,4]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])

    print(my_list)