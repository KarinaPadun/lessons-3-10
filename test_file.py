my_list = ['245', '567', '3578', '5645', '7564']
my_result = []

for i in range(len(my_list)):
    if i % 2 == 1:
        reversed_string = my_list[i][::-1]
        my_result.append(reversed_string)
    else:
        my_result.append(my_list[i])

print(my_result)
