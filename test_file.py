def new_list(i):
    n_list = [i if my_list.index(i) % 2 == 0 else i[::-1] for i in my_list]
    return n_list


my_list = ['245', 'rtyy', 'et', 'yyu', 'ttie']
result = new_list(my_list)
print(result)


def new_list(my_list):
    n_list = [s if my_list.index(s) % 2 == 0 else s[::-1] for s in my_list]
    return n_list


my_strings = ['245', 'rtyy', 'et', 'yyu', 'ttie']
result = new_list(my_strings)
print(result)


def new_list(list_1):
    n_list = [i if list_1.index(i) % 2 == 0 else i[::-1] for i in list_1]
    return n_list


my_list = ['245', 'rtyy', 'et', 'yyu', 'ttie']
result = new_list(my_list)
print(result)
