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
    else:




    return result


number_1 = float(input('Enter first number: '))
op = input ('Enter operator (+,-,*,/,^): ')
number_2 = float(input('Enter second number: '))
print(number_1,op,number_2)
result = calculate(number_1,number_2,op)
print('=',result)