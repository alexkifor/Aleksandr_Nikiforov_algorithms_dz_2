def reversed_num(num, result=''):
    if num == 0:
        print(result)
    else:
        return reversed_num(num//10, result + str(num % 10))

reversed_num(int(input('Введите число: ')))