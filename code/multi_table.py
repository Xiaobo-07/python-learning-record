'''
嵌套循环练习之九九乘法表
要求：
    按如下格式输出九九乘法表
    1x1=1
    1x2=2 2x2=4
    ...
    1x9=9 ... 9x9=81

Version: 0.1
Author: Xiaobo
'''

# for循环
for i in range(1,10):
    for j in range(i):
        print('{}x{}={}'.format(i,j+1,i*(j+1)), end=' ')
    print()

# while循环
m = 1
while m <= 9:
    n  = 1
    while n <= m:
        print('{}x{}={}'.format(m,n,m*n), end=' ')
        n += 1
    print()
    m += 1