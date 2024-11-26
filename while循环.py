# 死循环
# 基本格式
# while True:
    # 循环体
#while True: #条件只写True说明一直为真，一直执行，从而形成死循环
#    print('hhxx')

# 1.3 while循环应用：计算1+2+3+...+100的和
i = 1 #定义一个初始值
s = 0 #定义一个变量保存计算结果，最开始计算结果为0
while i <= 100:
    i += 1 #每循环一次i的值+1
    s = s + i
print(s)

# 2 while循环嵌套
# 2.1 含义：一个while循环里面有另一个while
# while 条件1:
#     循环体1
#     while 条件2：
#         循环体2
#         改变变量2
#     改变变量1
# 注意缩进决定层级，严格控制缩进，最好自动

a = 1 # 定义一个变量记录外循环的次数
while a <= 3:
    print(f"这是第{a}次外循环")
    b = 1
    while b <= 5:  #每执行一个外循环，会将内循环中所有的条件都循环一次，直到结束
        print(f"这是第{b}次内循环")
        b += 1
    a += 1