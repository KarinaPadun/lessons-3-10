def calculate(number_1 , number_2 , op):
    number_1 = None
    while number_1 is None:
        try:
            number_1 = float(input('Enter first number: '))
        except (ValueError, NameError):
            print('Error: enter a valid number')

    input('Enter operator (+, -, *, /, **): ')

    number_2 = None
    while number_2 is None:
        try:
            number_2 = float(input('Enter second number: '))
        except (ValueError, NameError):
            print('Error: enter a valid number')


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


#try:
 #   number_1 = float(input('Enter first number: '))

#except (ValueError,NameError):
 #   print('Error: enter number')
#except NameError:
    #number_1 = None
    #print("It shoud be a number")

#op = input('Enter operator (+,-,*,/,**): ')
#try:
     #number_2 = float(input('Enter second number: '))
#except(ValueError, NameError):
  #  print('Error: enter number')
#except NameError:
    #number_2 = None
    #print("It shoud be a number")





print(number_1,op,number_2)
result = calculate (number_1,number_2,op)
print('=' , result)


