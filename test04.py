name = '小明'
age = 18
print(f'我的名字叫{name}，今年{age}岁，请多多关照!')

print(name)  #name是变量名，print输出函数输出的是该变量名对应的变量值
print('name') #'name'代表字符串

student_no = 1  #整型数值不能以0开头
# 说明：整型的占位符为 %d,%06d表示整型必须是6位数，入伙不足6位，用0补齐
print('我的学号是 %06d' % student_no)

price = 9.00
weight = 5.00
money = price * weight
# %f 表示浮点型占位符 %.1f/%.2f表示保留几位小数点
print('苹果单价 %.1f 元/斤，购买了 %.1f 斤，需要支付 %.2f 元' % (price, weight, money))

