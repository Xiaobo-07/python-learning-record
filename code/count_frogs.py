'''
for循环练习之数青蛙
要求：
    1. 输出格式'x只青蛙x张嘴x个眼睛x条腿，扑通扑通跳下水'
    2. 输出1,2,3...,20
    3. 要求使用for循环
    4. 用range()函数产生数列

Version: 0.1
Author: Xiaobo
'''

for i in range(1,21):
    print('{}只青蛙{}张嘴{}个眼睛{}条腿，扑通扑通跳下水'.format(i,i,i*2,i*4))