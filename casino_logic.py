import  random
def bet(rate,amount,balance):
    lst = [i for i in range(1, 31)]
    win_rate = random.choice(lst)
    if win_rate == rate:
        print('Вы выиграли')
        return balance + amount
    else:
        print('Вы к сожелению проиграли')






