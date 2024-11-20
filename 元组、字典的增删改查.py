# 1. 元组
# 1.1 基本格式：元组名 = (元素1, 元素2, 元素3)
# 所有元素包含在小括号内，元素与元素之间用逗号隔开，不同元素也可以是不同的数据类型

tua = (1, 2, 3, 4, 5, 'a')  #tuple元组类型
print(type(tua))
tub = (1, )  #只有一个元素的时候末尾必须加","，否则返回唯一的值的数据类型，不输出tuple类型
print(type(tub))

# 1.2 元组与列表的区别
# 元组只有一个元素末尾必须加","，列表不需要
array1 = [1]
print(type(array1))
# 元组只支持查询操作，不支持增删改操作

tua = (1, 2, 3, 4, 1)
print(tua[2])   #元组也有下标，从0开始

# count、index、len跟列表的用法相同
print(tua.index(2))
print(tua.count(1))
print(len(tua))
print(tua[1:])

# 1.3 应用场景
# 函数的参数和返回值
# 格式化输出后面的()本质上就是一个元组
name = 'Johnny'
age = 22
print("%s的年龄是:%d" % (name, age))
# 数据不可以被修改，保护数据的安全


# 2 字典
# 2.1 基本格式  字典名 = {键1 : 值1, 键2 : 值2}
# 键值对形式保存，键和值之间用:隔开，每个键值对之间用,隔开
dic = {'name' : 'Johnny', 'age' : 22}
print(type(dic))
print(dic)
# 字典中的键具有唯一性，但是值可以重复
dic2 = {'name' : 'Johnny', 'name' : 22}  #不会报错，键名重复前面的值会被覆盖
print(dic2)

# 2.2 字典常见操作1
# 2.2.1 查看元素
# 变量名[键名]
dic = {'name' : 'Johnny', 'age' : 22}
print(dic['name'])   #不可以根据下标，字典中没有下标，查找元素需要根据键名

# print(dic['sex'])  #键名不存在则报错
# 变量名.get（键名）
print(dic.get('name'))
print(dic.get('sex', "没找到，沉淀沉淀吧"))  #键名不存在返回None，可自定义输出

# 2.2.2 修改元素
# 变量名[键名] = 新的值
dic = {'name': 'Johnny', 'age': 22}
dic['age'] = 20   #列表通过下标修改，字典通过键名修改

# 2.2.3 新增元素
# 变量名[键名] = 值
# 存在即修改，不存在则新增
dic = {'name': 'Johnny', 'age': 22}
dic['tel'] = 18678498849
print(dic)
dic['remark'] = "在线求偶"
print(dic)

# 2.2.4 删除元素
# 2.2.4.1 del
# 删除整个字典   del 字典名
dic = {'name': 'Johnny', 'age': 22}
# del dic
# print(dic)   #报错 字典不存在

# 删除指定键值对，键名不存在就会报错  del 字典名[键名]

del dic['name']
print(dic)
# del dic['name']   #键名不存在就会报错
# print(dic)


# 2.2.4.2 clear
# 清空整个字典里面的东西，但保留这个字典
dic = {'name': 'Johnny', 'age': 22}
dic.clear()
print(dic)

# 2.2.4.3 pop
# 删除指定键值对，键不存在就报错
dic = {'name': 'Johnny', 'age': 22}
dic.pop('age')   #必须指定键名
dic.popitem()   #3.7之前是随机删除一个键值对，之后则默认删除最后一个键值对
print(dic)

# 2.3 字典的常见操作2
# 2.3.1 len求长度
dic = {'name': 'Johnny', 'age': 22}
print(len(dic))  #返回键值对数量

# 2.3.2 keys返回字典里面包含的所有键名
dic = {'name': 'Johnny', 'age': 22}
print(dic.keys())
# for循环取出键名
for i in dic.keys():  #只取出键名
    print(i)

# 2.3.3 values返回字典里面包含的所有值
dic = {'name': 'Johnny', 'age': 22}
print(dic.values())
# for循环取出值
for i in dic.values():  #只取出值
    print(i)

# 2.3.4 items返回字典里包含的所有键值对,以元组形式
dic = {'name': 'Johnny', 'age': 22}
print(dic.items())
for i in dic.items(): print(i)  #i是元组类型

# 2.4 字典应用场景
# 使用键值对存储描述一个物体的相关信息