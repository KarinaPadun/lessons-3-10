#1
#a виведіть третій символ цього рядка.
value_str = 'ttyrtg'

for letter in value_str:
    if value_str.index(letter) == 2:
         print(letter)

#b виведіть передостанній символ цього рядка.

value_str = 'rtyuio'

for letter in value_str:
    if value_str.index(letter) == -1:
         print(letter)