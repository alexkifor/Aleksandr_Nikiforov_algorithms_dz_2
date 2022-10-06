def sum_n(n, count=0, num=1, sum=0):
    if count == n:
        print(f'сумма {n} чисел равна {sum}')
    else:
        return sum_n(n, count+1, -num/2, sum + num)

sum_n(n=int(input('введите n: ')))