# 1 集合
# 1.1 基本格式：集合名 = {元素1, 元素2, 元素3}
s1 = {1, 2, 3}
s2 = {}   #定义空字典
s3 = set()  #定义空集合
print(s1)
print(s2)
print(type(s3))

# 1.2 集合无序性
s4 = {1, 'a', 'r', 'G', 4, 9, 'E'}
print(s4)   #每次运行结果都不一样
s5 = {1, 2, 3, 4, 5}   #纯数字有序
print(s5)

# 集合无序的实现方法涉及hash表
print(hash('a'))  #每次运行结果都不同，hash值不同，那么在hash表中的位置就不同，这就实现了集合的无序

# 利用无序性，不能修改集合中的值

# 1.3 集合具有唯一性，可以自动去重
s1 = {1, 2, 3, 4, 5, 9, 6, 3}
print(s1)

# 1.4 集合的常见操作
# 1.4.1 添加元素
# add 添加的是一个整体
s1 = {1, 2, 3, 4, 5, 9, 6, 3}
print("原集合：", s1)
s1.add(7)   #如果已经存在不进行任何操作，且一次只能添加一个元素
s1.add((1, 2)) #只能使用一个元组作为一个整体
print("现集合：", s1)