'''
if 语句练习之成绩转换
要求：
    1. 将百分制成绩转换为等级制(优+，优-，良，及格，不及格)
    2. 各分数段对应的等级如下
        优+       90及以上
        优-       80 - 89（含80,89）
        良        70 - 79（含70,79）
        及格      60 - 69（含60,69）
        不及格    59及以下

Version: 0.1
Author: Xiaobo
'''

grade = int(input('请输入成绩：'))
if grade >= 90:
    print('优+')
elif grade >= 80:
    print('优-')
elif grade >= 70:
    print('良')
elif grade >= 60:
    print('及格')
else:
    print('不及格')