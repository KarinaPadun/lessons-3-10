# порівняння list та tuple
# змінні не змінні типи даних різниця
# методи строк(split(), rsplit(), join())
# методи list(append(), pop(), sort(), copy())
# функція sorted()

# list = () - cписки , масиви
# tuple = () - кортеж, є незмінний , зустрічаються в бібліотеках та константах

value_list = [1 , 1.1 , '&',None , True , [1]]
value_tuple = (1 , 1.1 , '&',None , True , [1])

#####################################################

base_list = [1, 2, 3]
my_new_list = base_list * 4
print(my_new_list)
base_list[0] = 10
print(f"base_list {base_list}")
print(f"my_new_list {my_new_list}")

#####################################################
base_list = [1, 2, 3]
my_new_list = [base_list] * 4
print(my_new_list)
base_list[0] = 10
print(f"base_list {base_list}")
print(f"my_new_list {my_new_list}")