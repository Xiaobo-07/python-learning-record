'''
练习：游戏英雄联盟
要求：
    输入角色：xxx
    输入拥有的装备：xxx
    输入想购买的装备：xxx
    输入付款金额：xxx
    输出：xxx拥有xxx装备花了xxx金币
Version: 0.1
Author: Xiaobo
'''

#提示信息
print('''
***************************
     League of Legend
***************************
''')

role = input('输入角色:')
equipment = input('输入拥有的装备:')
upgrade_equipment = input('输入想购买的装备:')
pay = int(input('输入付款金额:'))
equipment = upgrade_equipment

print('{}拥有{}装备，购买此装备花了{}金币。'.format(role,equipment,pay))