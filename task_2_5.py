def table_ascii(n=32, count=0):
    if n == 128:
        print()
    elif count == 10:
        print()
        return table_ascii(n, count=0)
    else:
        print(f'{n} - {chr(n)}', end=' ')
        n += 1
        count += 1
        return table_ascii(n, count)

table_ascii()