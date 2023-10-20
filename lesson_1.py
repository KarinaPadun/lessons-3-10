#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])


value_str = "hello i am helena. I have a cat"


first_h_position = value_str.find("h")
last_h_position = value_str.rfind("h")


result_str = value_str[:first_h_position + 1] + value_str[first_h_position + 1:last_h_position].replace("h", "H") + value_str[last_h_position:]

print(result_str)
