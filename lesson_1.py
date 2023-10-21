#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])

my_list = [-5,4,3,1]
my_list.append(0 if len(my_list) < 2 else my_list[-1] + my_list[-2])
print(my_list)
