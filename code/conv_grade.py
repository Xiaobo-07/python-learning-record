'''
if 语句练习之成绩转换
要求：
    1. 输入一个百分制成绩，然后将成绩输出为等级
	2. 各等级对应的成绩段如下:
		优+     >=90
		优-     >=80, <90
		良      >=70, <80
		及格    >=60, <70
		不及格  <60

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