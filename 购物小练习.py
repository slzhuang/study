'''
课堂练习：某超市T恤的单价为56.5，裤子的单价是89.8。
        凤姐买了3件T恤，5条裤子，请写程序计算凤姐一共该给多少钱？
        如果是老板过生日，全场88折，凤姐需要福多少钱？
'''

# 1. 定义变量，接受用户的输入
t_shirt = float(input('请输入T恤的单价: '))
pants = float(input('请输入裤子的单价: '))

t_shirt_count = int(input('买了几件T恤? '))
pants_count = int(input('买了几条裤子? '))

# 2.数值运算
normal_price = t_shirt * t_shirt_count + pants * pants_count
print(f'一共消费了{normal_price}')
discount = 0.88
discount_price = normal_price * discount
print(f'打折后花了{discount_price}')