def get_number(prompt):
    while True:
               try:
                    number = float(input(prompt))
                    if number.is_integer():
                        return int(number)
                    return number
               except ValueError:
                print("Это не число!")

def get_operation():
    message = '''
    Выберите математическую операцию:

    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение
    Ваш выбор:
    '''
    correct_operations = '+-/*'
    operation = input(message)
    while operation not in correct_operations:
         print('Такая операция недоступна, повторите попытку.')
         operation = input(message)
    return operation

def calculate(num_1, num_2, operation):
    result = None
    if operation == '+':
       result = num_1 + num_2
    elif operation == '-':
          result = num_1 - num_2
    elif operation == '/':
          try:
              result = num_1 / num_2
          except ZeroDivisionError:
           result = "Нельзя делить на ноль!"
    elif operation == '*':
          result = num_1 * num_2
    return result

def main():
    num_1 = get_number("Введите первое число: ")
    num_2 = get_number("Введите второе число: ")
    operation = get_operation()
    result = calculate(num_1, num_2, operation)
    print("Результат: ", result)

main()
while True:
    decision = (input('Продолжить? (1 = да; 2 = нет) ')).lower()
    if decision == '1':
        main()
    elif decision == '2':
        break


