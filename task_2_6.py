from random import randint
def guess_num(random_num=randint(1, 100), count=1):
    num = random_num
    user_num = int(input('введите число от 1 до 100: '))
    if count == 10:
        print('вы не угадали число!')
    else:
        if num == user_num:
            print('Вы отгадали число!')
        elif num > user_num:
            print('введите большее число')
            return guess_num(random_num=num, count=count+1)
        else:
            print('введите меньшее число')
            return guess_num(random_num=num, count=count + 1)

guess_num()