'''
练习：日期显示输出
要求：
    1. 依次从键盘输入年，月，日然后输出对应日期
    2. 输出格式示例：January 6th, 2020
    3. 用列表存放月份以及日期后的结尾'st nd rd th'

Version: 0.1
Author: Xiaobo
'''

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
endings = ['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] + 7*['th'] + ['st']

year = input('Year:')
month = int(input('Month(1-12):'))
day = int(input('Day(1-31):'))

month_name = months[month - 1]
ordinal = str(day) + endings[day - 1]

print(month_name + ' ' + ordinal + ', ' + year)