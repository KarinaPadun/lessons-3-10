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
result_str = value_str[:-2]
print(result_str)

#rfind
#string[::-1]

#value_str = 'rtyuio'

 #for value_str range(0,6):
  #  print(value_str) string[ : 5 ]



#i. виведіть довжину цього рядка.

value_str = 'yr6uiooo'

if len(value_str):
    print(len(value_str))