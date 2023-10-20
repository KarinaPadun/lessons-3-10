#1
#a виведіть третій символ цього рядка.
value_str = 'ttyrtg'

for letter in value_str:
    if value_str.index(letter) == 2:
         print(letter)

#b виведіть передостанній символ цього рядка.

value_str = 'rtyuio'

print(value_str[-2])

#b2 виведіть передостанній символ цього рядка.
value_str = 'rtyuto'
for i in range(len(value_str)):
    if i == len(value_str) - 2:
        print(value_str[i])
#c.виведіть перші п'ять символів цього рядка.
value_str = 'rtyuiocvb'
print(value_str[:5])
#c.2 виведіть перші п'ять символів цього рядка.
value_str = 'rtyuiocvb'
for i in range(5):
    print(value_str[i])
#d виведіть весь рядок, крім двох останніх символів.
value_str = 'rtyuiocvb'
result = value_str[:-2]
print(result)
#d2. виведіть весь рядок, крім двох останніх символів.
#value_str = 'rtyuiocvb'

#for i in range(len(value_str) - 2):
    #print(value_str[i], end='')
# e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)

value_str_1 = 'hgfd3t'
print(value_str_1[::2])

# e2. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)
value_str_1 = 'hgfd'
for i in range(0, len(value_str_1), 2):
    print(value_str_1[i])
# f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
value_str_1 = 'hgfd3t'
print(value_str_1[1::2])
# f2. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
value_str_1 = 'hgfd'
for i in range(1, len(value_str_1), 2):
    print(value_str_1[i])
# g. виведіть усі символи у зворотному порядку.
value_str_2 = 'Teyr'
print(value_str_2[::-1])

# g2. виведіть усі символи у зворотному порядку.
value_str_3 = 'Yuio'
for i in range(len(value_str_3)-1,-1,-1):
    print(value_str_3[i])
# h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
value_str_4 = 'Yuiot'
for i in range(len(value_str_4) - 1, -1, -2):
    print(value_str_4[i])
# h2. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
value_str_5 = '123456'
i = value_str_5 [::-1][::2]
print(i)
#i. виведіть довжину цього рядка.

value_str = 'yr6uiooo'

if len(value_str) > 0:
   print(len(value_str))

# i2. виведіть довжину цього рядка.
value_str = 'yr6uiooo'
print(len(value_str))


# 2

value_str = 'my name is Eric'
words = value_str.split()
k = len(words)
print('кількість слів у рядку:',k)

value_str = 'my name is Eric, i am 13'

k = value_str.count(' ') + 1
print('кількість слів у рядку:', k)

# 3
while True:
 s= input('Введіть рядок : ')
 ch = input('Введіть один символ: ')

# find для знаходження першого вміщення символу ch
 first_placement = s.find(ch)

#  rfind для знаходження останнього вміщення символу ch
 last_placement = s.rfind(ch)

 if first_placement != -1:
    print(f"Перше входження символу '{ch}' знайдено на позиції {first_placement}.")
 else:
    print(f"Символ '{ch}' не знайдено у рядку '{s}'.")

 if last_placement != -1:
    print(f"Останнє входження символу '{ch}' знайдено на позиції {last_placement}.")
 else:
    print(f"Символ '{ch}' не знайдено у рядку '{s}'.")
 input('Продовжити пошук? (y/n): ')

 if continue_search.lower() != 'так':
     break

#4. Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.
value_str = ("hello i am helena")