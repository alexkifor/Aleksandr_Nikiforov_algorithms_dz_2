def calculator(a=0, b=0):
    operator = input('введите +, -, *, / или 0 для выхода: ')
    if operator in ('+', '-', '*', '/', '0'):
        if operator != '0':
            try:
                a = int(input('введите первое число: '))
                b = int(input('введите второе число: '))
            except ValueError:
                print('введено не число')
                calculator(a, b)
            if operator == '/' and b == 0:
                while True:
                    try:
                        b = int(input('введите число отличное от 0: '))
                    except ValueError:
                        print('введено не число')
                    else:
                        if b == 0:
                            print('деление на ноль невозможно')
                        else:
                            print(f'частное от деления числа {a} на число {b} равно {a / b}')
                            break
                calculator(a, b)
            elif operator == '/':
                print(f'частное от деления числа {a} на число {b} равно {a / b}')
                calculator(a, b)
            elif operator == '+':
                print(f'Сумма чисел {a} и {b} равна {a + b}')
                calculator(a, b)
            elif operator == '*':
                print(f'Произведение чисел {a} и {b} равно {a * b}')
                calculator(a, b)
            elif operator == '-':
                print(f'Разность чисел {a} и {b} равна {a - b}')
                calculator(a, b)
        else:
            print('Завершение работы')
    else:
        print('введен недопустимы оператор, попробуйте снова')
        calculator(a, b)

calculator()








