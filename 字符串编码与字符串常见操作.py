# Unicode：所有字符都是两个字节
# 好处：字符与数字之间转换速度更快
# 坏处：浪费空间

# UTF-8：精准，对不同的字符用不同的长度表示
# 好处：节省空间
# 坏处：字符与数字之间转换速度更慢，每次都需要计算字符要用多少字节来表示
# 1.解码
a = 'hello'
print(a, type(a))  #字符串
a1 = a.encode()
print("格式为：", type(a1), "编码后为：", a1)
a2 = a1.decode()
print("格式为：", type(a2), "解码后为：", a2)

st = "你好"
st1 = st.encode("utf-8")
print(st1)
st2 = st1.decode("utf-8")
print(st2)
# 2.字符串常见操作
# 2.1 字符串拼接
print(10 + 10)  # +为算数运算符
print("10" + ' 10')  #字符串相加，+是字符串拼接
name1 = "你好"
name2 = "牛"
print(name1, name2, sep="")  #等同下
print(name1 + name2)

# 2.2 * 算数运算符 字符串中为重复输出

print("测试重复输出\n" * 5)
# 注意：需要输出多少次*后面就写多少
print('&' * 10)

# 2.2 成员运算符
# 作用：检查字符串中是否包含了某个子字符串(即某个字符或多个字符)
# in : 如果包含的话返回True，不包含返回False
# not in : 如果不包含的话返回True，包含返回False
name = "binding"
print('b' in name)
print('b' not in name)
print('a' in name)
print('a' not in name)
print('bin' in name)
print('bin' not in name)

name = "刘霖" #支持中文

print('a' in name)
print('刘霖' in name)

# 2.3 下标/索引
# Python中下标从0开始
# 作用：通过下标能够快速找到对应的数据
# 格式：字符串名[下标符]
name = 'six star'
print(name[0])
# 从右往左是-1开始
print(name[-1])

# 2.4 切片
# 含义：指对操作的对象截取一部分的操作
# 语法：[开始位置:结束位置:步长]
# 也遵循包前不包后原则:即从起始位置开始，到结束位置的前一位结束(不包含结束位置本身)
st = 'abcdefghigklmn'
print(st)
print(len(st))
print(st[0:4])
print(st[4:7])
print(st[7:]) #7后的全部截取
print(st[:7]) #7前的全部截取

# 从右往左
print(st[:-1])  #会相反
# 步长：表示选取间隔，不写步长默认为1
# 步长的绝对值大小决定切取的间隔，正负号决定切取方向
# 正数表示从左往右取值，负数表示从右往左
print(st[-1::-1])
print(st[0:7:3])