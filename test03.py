'''
    Python中有哪些数据类型？
    格式：
        变量名 = 变量值
'''
# 1.整形数据  int
num1 = 999
# print(f'num1 = {num1}')  输出的固定格式，f -> format格式化，特点就是在单引号字符串中能够书写{}，大括号中可以放入'变量名'
print(f'num1 = {num1}')

# 定义一个变量
name = 'zhuangsulei'

print(name)

names = ['望月' , '王悦' , '王越']
print(f'{names[0]},{type(names)}')
# 元组
names = ('望月' , '王悦' , '王越')
print(f'{names[0]},{type(names)}')
# 集合类型 ：特点，无序，不可重复，可拓展。
# 无序：内部是通过一套算法实现，可能使用到了当前时间戳变量
names = {'望月' , '王悦' , '王越' , '王越'}
print(f'{names},{type(names)}')
# 字典类型：key -> value
stu_dict = {'stu_id':'1000' , 'name':'王越'}
print(f'{stu_dict},{type(stu_dict)}')