def calculate(number_1 , number_2 , op):

  if op == '+':
        result = number_1 + number_2
  elif op == '-':
        result = number_1 - number_2
  elif op == '*':
        result = number_1 * number_2
  elif op == '/':
    if number_2 != 0:
       result = number_1 / number_2
    else:
       return "Error: division by zero"

  elif op == '**':
        result = number_1 ** number_2
  else:
       return "Error: invalid statement"
  return result

number_1 = float(input('Enter first number: '))

op = input('Enter operator (+,-,*,/,**): ')

number_2 = float(input('Enter second number: '))

print(number_1,op,number_2)
result = calculate (number_1,number_2,op)
print('=' , result)


