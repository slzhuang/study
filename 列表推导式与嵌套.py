# 1.1 列表推导式
# 格式一 [表达式 for 变量 in 列表]
# 注意：in后面不仅可以放列表，还可以放range、可迭代对象
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[print(i) for i in array1]   #前面的i为表达式

array2 = []

for i in range(10):
    array2.append(i)
    print(array2)

[array2.append(i) for i in range(6)]
print(array2)

# 格式二 [表达式 for 变量 in 列表 if 条件]
# 把基数放到列表里面
array3 = []
for i in range(5):
    if i % 2 == 1:
        array3.append(i)
print(array3)

[array3.append(i) for i in range(5) if i % 2 == 1]
print(array3)

# 1.2 列表嵌套
# 含义：一个列表里面又有一个列表

array4 = [1, 2, 3, [7, 8, 9]]  #[7, 8, 9]是里面的列表
print(array4[3])   #会取出里面的列表
print(array4[3][1])  #再加一个[]表示取出内列表里的相应下标元素
