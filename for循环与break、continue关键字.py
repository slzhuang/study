# for循环基本格式
# for 临时变量 in 可迭代对象:
#     循环体
# 注意冒号和缩进

str = "hellopython"  #定义一个字符串,字符串为可迭代对象
print(type(str))
for i in str:
    print(i)

# 计数函数range()，用来记录循环次数，相当于计数器
# 参数range(start,stop,step)
for i in range(1,6): #从1开始，从6结束，包前不包后
    print(i)
s = 0
for i in range(1,101):
    s += i
print("计算结果为：",s)

# break和continue循环中的关键字

i = 1
while i <= 5:
    print(f"黑皮在吃第{i}个苹果")
    if i == 3:
        print("黑皮吃饱了不吃了")
        break  #直接跳出整个循环
    i += 1

e = 1
while e <= 5:
    print(f"黑皮又吃了这一堆的第{e}个苹果")
    if e == 3:
        print(f"黑皮吃了一嘴虫子，第{i}个扔了")
        e += 1
        continue #跳过当前的循环，但不跳出整个循环
    e += 1
