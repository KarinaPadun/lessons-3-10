#print("hello world")

#value ="123456789"

#my_str = value if len(value) < 5 else value[1::2]

#print(my_str[::-1])


s = input("Введіть рядок s: ")
ch = input("Введіть символ ch: ")

count = 0
index = -1

while True:
    index = s.find(ch, index + 1)
    if index == -1:
        break
    count += 1

print(f"Символ '{ch}' зустрічається {count} разів у рядку '{s}'.")