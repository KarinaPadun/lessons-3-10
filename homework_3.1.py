def calculate(num_1, num_2, op):
    if op == '+':
        result = num_1 + num_2
    elif op == '-':
        result = num_1 - num_2
    elif op == '*':
        result = num_1 * num_2
    elif op == '/':
        if num_2 != 0:
            result = num_1 / num_2
        else:
            return "Error: division by zero"
    elif op == '**':
        result = num_1 ** num_2
    else:
        return "Error: invalid statement"
    return result


continue_calculating = True

while continue_calculating:
    number_1 = None
    while number_1 is None:
        try:
            number_1 = float(input('Enter first number: '))
        except (ValueError, NameError):
            print('Error: enter a valid number')

    op = input('Enter operator (+, -, *, /, **): ')

    number_2 = None
    while number_2 is None:
        try:
            number_2 = float(input('Enter second number: '))
        except (ValueError, NameError):
            print('Error: enter a valid number')

    print(number_1, op, number_2)
    result = calculate(number_1, number_2, op)
    print('=', result)

    yes_or_no = input('Continue? (y/n): ').lower()
    if yes_or_no != 'y':
        continue_calculating = False
