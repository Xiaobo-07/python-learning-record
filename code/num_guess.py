'''
while循环练习之猜数字
要求：
    1. 从1~99中产生随机数字 answer_num
    2. 用户可以从键盘输入猜测的数字 user_guess
    3. 判断用户输入的数字是否猜中
    4. 若用户没有猜中数字则输出提示并不断缩小范围，直到用户猜中数字为止
    5. 记录用户猜中数字用的次数并输出

Version: 0.1
Author: Xiaobo
'''

#加载random模块，需要用到random模块中的函数来产生随机数
import random

answer_num = random.randint(1,99)
min_num = 1
max_num = 99
count = 0
print('0~99猜数字')
while True:
    user_guess = int(input('请输入数字:'))
    count += 1
    if user_guess < answer_num:
        print('答案在{}~{}之间'.format(user_guess, max_num))
        min_num = user_guess
    elif user_guess > answer_num:
        print('答案在{}~{}之间'.format(min_num, user_guess))
        max_num = user_guess
    else:
        print('恭喜你猜中啦！共猜了{}次'.format(count))
        break
    