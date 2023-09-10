#用系统随机生成一个数，玩猜数游戏 数字最好在1-10
#这道题用方法写，可以写成一个简单的demo例子
import random as rd
def guessNumber():
    inputNumber = int(input('猜一个数吧：'))
    if inputNumber < randomNumber:
        print('猜小了，重猜一下！')
        guessNumber()
    if inputNumber == randomNumber:
        print('恭喜你，猜对了！')
    if inputNumber > randomNumber:
        print('猜大了，重猜一下！')
        guessNumber()
randomNumber = rd.randint(1,10)
guessNumber()

