'''
字符串，整型，浮点型之间的类型转换 ：
格式：
    1.整型 int(变量)
    1.浮点型 float(变量)
    1.字符串类型 str(变量)
'''

# 字符串类型
num1 = '10'
num2 = '20'
# 字符串 + 字符串 = 两个字符串相拼接
# 网页中的输入框 ：input标签（网页中的输入框获取的数据都是字符串类型的）
result = num1 + num2
print(f'result = {result}')

# 需求：将字符串类型转换为整型
n1 = int(num1)
n2 = int(num2)
# int + int 为数学运算
result = n1 + n2
print(f'str转换int的result为 {result}')

# float 浮点型
f1 = 66.66
f2 = 88.88
result = f1 + f2
print(f'浮点型计算为{result}')
# 浮点型转换为整型是直接丢弃掉小数部分(数据精度丢失)
i1 = int(f1)
i2 = int(f2)
result = i1 + i2
print(f'浮点型转换int的result为 {result}')  # 66 + 88 = 154