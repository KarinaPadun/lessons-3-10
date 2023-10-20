#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])

my_string = '0123456789'

number = 0
while number < 100:
    num_str = my_string[number // 10] + my_string[number % 10]
    num_int = int(num_str)
    print(num_int)
    number += 1


string = '0123456789'

tens_digit = 0
while tens_digit < 10:
    ones_digit = 0
    while ones_digit < 10:
        num_str = string[tens_digit] + string[ones_digit]
        num_int = int(num_str)
        print(num_int)
        ones_digit += 1
    tens_digit += 1