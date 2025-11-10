try:
    num1 = int(input("Введите первое число "))
    num2 = int(input("Введите второе число "))

    result = num1 / num2
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа закрывается!")

