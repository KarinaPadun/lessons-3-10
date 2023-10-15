###############################################1
value = 101 #value = int()

new_value = value / 2 if value < 100 else -value
print(new_value)
###############################################2
value = 10 #value = int()

new_value = 1 if value < 100 else 0
print(new_value)
########################################################3
value = 10 #value = int()

new_value = True if value < 100 else False
print(new_value)
########################################################4
my_str = "fyf"

new_str = my_str + my_str if len(my_str) < 5 else my_str
print(new_str)
########################################################5
my_str = "123"

new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)

