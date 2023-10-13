
#n_1 = int (input('Введіть число 1:'))
#n_2 = int(input('Введіть число 2:'))

#operator = int (input('Яку операцію Ви хочете виконати? \n 1 "+" \n 2 "-" \n 3 "*" \n 4 "/"'))

#if r == 1 :
    #result = n_1 + n_2

#print('Результат == result')





inp = float(input('Welcome, please enter a number : '))
print('You entered: ' ,inp)

def calculate(number_1,number_2,op):
    if op == '+':
        result = number_1+number_2
    elif op == '-':
        result = number_1-number_2
    elif op == '*':
        result = number_1*number_2
    elif op == '/':
        result = number_1/number_2
    elif op == '^':
        result = number_1**number_2
    return result


number_1 = float(input('Enter first number: '))
op = input ('Enter operator (+,-,*,/,^): ')
number_2 = float(input('Enter second number: '))
print(number_1,op,number_2)
result = calculate(number_1,number_2,op)
print('=',result)