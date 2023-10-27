# print("hello world")

my_list = [2, 0, 3, 4]
new_list = [i for i in my_list if my_list.index(i) != 0]

new_list.append(my_list[0])
print(new_list)

# 4.1

my_list = [2, 0, 3, 4]
new_list = []

for i in my_list[1:]:
    new_list.append(i)

new_list.append(my_list[0])

print(new_list)




