def sum_n(n, count=0, sum=0):
    if n == count:
        return (sum + count)
    else:
        return sum_n(n, count + 1, sum + count)

n = int(input('введите число: '))
print(sum_n(n))
print(n * (n + 1) / 2)
print(sum_n(n) == n * (n + 1) / 2)