# print("hello world")


my_list_1 = [-3, 3, -455, 20, 114]
my_list_2 = [3, 0, 9, 4, 8, 11]
my_result = [i for i in my_list_1[::2]]
my_result.extend(my_list_2[::2])
print(my_result)