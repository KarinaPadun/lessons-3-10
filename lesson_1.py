#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])

my_list = [2, 0, 3, 4]
new_list = []

for i in my_list[1:]:
    new_list.append(i)

new_list.append(my_list[0])

print(new_list)

