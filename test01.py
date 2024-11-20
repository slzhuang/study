'''
    转义字符 ：
        t 字符t       \t 水平制表符(类似四个空格)
        n 字符n       \n 换行符
        \ 字符反斜杠   \  转义字符
'''

# print输出函数，默认会自动换行
print('hello', end='')  #end=空字符串可以不换行
print('world')

print('hello', end='\t')
print('world')

#print函数可以跟多个变量
num1 = 10
num2 = 20
num3 = 30
print(num1,num2)

#print(f'')
print(f'num1 = {num1},num2 = {num2}')

# .format()填充参数
print('num1 = {0}, num2 = {1}, num3 = {2}'.format(num1,num2,num3))