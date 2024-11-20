'''
    input 是 python 语言提供的输入函数
    格式：
        input(提示信息) 该函数会返回用户在键盘中输入的结果，但一定要小心。因为返回的结果都是str类型的
    说明：
        由于 input 输入函数会返回结果，所以程序中必须要定义一个变量接受 input 函数的结果
        input 是一个阻塞函数。如果用户不输入，程序就不会继续向下执行
'''

name = input('请输入您的姓名: ')
age = input('请输入您的年龄: ')
gender = input('请输入您的性别：')
print(f'我叫{name},今年{age}岁,{gender}')
# 求和,input 输入函数返回的是 str 类型结果
num1 = input('请输入第一个整型数值: ')
num2 = input('请输入第二个整型数值: ')
# sum求和
sum = int(num1) + int(num2)
print(f'sum = {sum}')