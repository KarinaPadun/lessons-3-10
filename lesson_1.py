#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])


my_list_1 = [-3, 3, -455, 20, 114]
my_list_2 = [3, 0, 9, 4, 8, 11]
my_result = []

for i in my_list_1:
    if my_list_1.index(i) % 2 == 0:  #
        my_result.append(i)

for i in my_list_2:
    if my_list_2.index(i) % 2 == 0:
        my_result.append(i)

print(my_result)
