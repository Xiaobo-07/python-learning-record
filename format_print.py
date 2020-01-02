'''
需求：看电影订单信息打印
movie : 我和我的祖国
count : 35
price : 39.9

输出结果：
电影：xxx
票价：xxx
人数：xxx
总价：xxx

Version: 0.1
Author: Xiaobo
'''

movie = '我和我的祖国'
ticket_price = 39.9
count = 35
price_count = ticket_price * count

#方法一
# print('电影：%s\n票价：%.1f元\n人数：%d\n总价：%.1f元' % (movie, ticket_price, count, price_count))

#方法二
# message = '''
# 电影：%s
# 票价：%.1f元
# 人数：%d
# 总价：%.1f元
# ''' % (movie,ticket_price,count,price_count)
# print(message)

#方法三
message = '''
电影：{}
票价：{}元
人数：{}
总价：{}元
'''.format(movie,ticket_price,count,price_count)
print(message)