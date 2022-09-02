# 猜数游戏：游戏一直运行，直到猜中正确的数
from operator import truediv


number = 35
running = True
while running:
    guess = int(input("请输入猜测的数："))
    if guess == number:
        print("正确")
        running = False
    elif guess < number:
        print("偏小")
    else:
        print("偏大")
