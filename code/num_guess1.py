'''
for循环练习之猜数字游戏
要求：
	1. 从1~10中随机产生一个数字
	2. 玩家可以从键盘输入数字进行猜测
	3. 玩家共有3次机会
	4. 如果玩家输入的数字超出答案范围(1~10)则警告
	5. 每次输入前提示玩家剩余次数

Version: 0.1
Author: Xiaobo
'''

import random

answer_num = random.randint(1,10)
count = 3 # 记录剩余次数
print('1~10猜数字')
for i in range(3):
    print('剩余{}次机会'.format(count))
    num_guess = int(input('输入猜测数字:'))
    if num_guess == answer_num:
        print('恭喜你，猜对了')
        break
    elif num_guess < 1 or num_guess > 10:
        print('请输入1~10内的数字')
    count -= 1
    if count == 0:
        print('很遗憾，游戏结束')