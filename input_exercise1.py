'''
游戏：捕鱼达人
要求：
    1.输入用户名
    2.输入密码
    3.充值初始金额
    ……
Version: 0.1
Author: Xiaobo
'''

#提示信息
print('''
***************************
         捕鱼达人
***************************
''')
#数据库中用户信息
u_name = 'Xiaobo'
u_password = '123456'
#输入用户信息
while True:
    user_name = input('请输入用户名:')
    user_password = input('请输入密码:')
    if u_name == user_name:
        if u_password == user_password:
            break
        else:
            print('密码错误')
    else:
        print('用户名未注册')
print('亲爱的%s,您的余额不足' % user_name)
user_coins = int(input('请输入充值金额:'))
print('充值成功,当前余额%d' % user_coins)

    