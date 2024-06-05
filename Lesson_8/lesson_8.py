from custom_exception import UnknownOperationError, NotANumberError


def summ(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    return x / y


def power(x, y):
    return x ** y


def main():
    while True:
        try:
            operation = input("Выберите операцию (+, -, *, /, **) или введите 'exit' для выхода: ")
            if operation == 'exit':
                break
            if operation not in ['+', '-', '*', '/', '**']:
                raise UnknownOperationError("Выбрана неизвестная операция.")
            x = input("Введите первое число: ")
            if not x.isdigit():
                raise NotANumberError("Это не число!")
            y = input("Введите второе число: ")
            if not y.isdigit():
                raise NotANumberError("Это не число!")
            x = int(x)
            y = int(y)
            if operation == '+':
                result = summ(x, y)
            elif operation == '-':
                result = minus(x, y)
            elif operation == '*':
                result = multiply(x, y)
            elif operation == '/':
                result = divide(x, y)
            elif operation == '**':
                result = power(x, y)

            print("Выражение равняется: ", result)
        except(UnknownOperationError, NotANumberError) as error:
            print("Ошибка: ", error)
        except ZeroDivisionError as error:
            print("Ошибка: ", error)


main()