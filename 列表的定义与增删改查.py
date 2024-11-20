# 1 列表
# 基本格式：列表名 = [元素1, 元素2, 元素3]
# 所有元素放在中括号内，元素与元素之间","间隔，元素之间的数据类型可以各不相同
array1 = [1, 'a', '3.14', 4, 5]
print(array1)
print(array1, type(array1))
# 切片操作
print(array1[0:3])
# 列表是可迭代对象，可以for循环遍历取值
for i in array1:
    print(i)

# 2 列表的常见操作
# 2.1 添加元素
# append extend insert
array2 = [1, 'a', '3.14', 4, 5]
print(array2)
array2.append("six")  #append为整体添加
print(array2)
array2.extend("seven")  #extend为分散体那家，会将添加的元素逐一添加
print(array2)

array3 = [1, 'a', '3.14', 4, 5]
print(array3)
array3.insert(0, "one")  #指定位置如果有元素，原有元素往后移，必须指定位置
print(array3)

# 2.2 修改元素
# 直接通过下标就可以进行修改

array4 = [1, 2, 3]
print(array4)
array4[1] = 'two'
print(array4)

# 2.3 查找元素
# in:判断指定元素是否存在列表中，如果存在的话返回True，不存在返回False
# not in:判断指定元素是否不存在列表中，如果不存在的话返回True，存在返回False
array5 = ['a', 'b', 'c']
print('b' in array5)
print('b' not in array5)
print('d' in array5)
print('d' not in array5)

# 案例：用户输入昵称，昵称重复则不能使用
# 定义列表，保存已经存在的昵称


# while True:
#     name_list = ['zhuangsulei0121', 'Johnny2002']
#     input_name = input("请输入您的名称：")
#     if input_name in name_list:
#         print(f"您输入的昵称{input_name}已经存在")
#     else:
#         print(f"昵称{input_name}注册成功")
#         # 昵称新增到列表
#         name_list.append(input_name)
#         print(name_list)
#         break

# index返回指定数据所在位置下标，如果查找数据不存在报错
# count统计指定数据在当前列表出现的次数
# 跟字符串中的用法相同

# 2.4 删除元素
# del
array6 = [1, 2, 3]
del array6[0]
print(array6)
del array6  #删除列表

# pop 删除指定下标的数据，py3版本默认是删除最后一个元素
array7 = [1, 2, 3]
array7.pop()
array7.pop(1)  #不能指定元素删除，只能根据下标进行删除
print(array7)

# remove 根据元素的值进行删除
array8 = [1, 2, 3, 4, 4, 4]
array8.remove(4)   #默认删除最开始出现的指定元素
print(array8)

# 2.5 排序
# sort 将列表按特定顺序重新排列，默认从小到大
array9 = [1, 4, 9, 5, 7]
array9.sort()   #从小到大排序
print(array9)

# reverse 倒序，将列表倒置（反过来）
array9.reverse()
print(array9)