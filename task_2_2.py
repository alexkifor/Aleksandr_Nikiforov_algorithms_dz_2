def check_even_odd_num(num, even=0, odd=0):
    if num == 0:
        print(f'четных числел {even}, нечетных числе {odd}')
    else:
        if num % 10 % 2 == 0:
            return check_even_odd_num(num//10, even + 1, odd )
        else:
            return check_even_odd_num(num//10, even, odd + 1)

check_even_odd_num(int(input('Введите число: ')))


