# 1 字符串常见操作
# 1.1 查找
# 1.1.1 find:检测某一个子字符串是否包含在字符串中，如在就返回这个字符串开始位置的下标，否则就返回-1
# find(子字符串, 开始位置下标, 结束位置下标)
# 注意：开始位置下标和结束位置下标可以省略，代表在整个字符串查找
# 同样包前不包后
name = 'niuniuniu'
print(name.find('i'))  # 第一个"i"的下标为1
print(name.find('niu'))  # n的下标为0
print(name.find('b', 3))
print(name.find('n', 3, 6))
# 1.1.2 index:检测某一个子字符串是否包含在字符串中，如在就返回这个字符串开始位置的下标，否则就会报错
# index(子字符串, 开始位置下标, 结束位置下标)
# 注意：开始位置下标和结束位置下标可以省略，代表在整个字符串查找
# 同样包前不包后
name = '你十大十大算法'
print(name.index('十'))
# print(name.index('我'))  #代码运行报错

# 1.1.3 count:返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串, 开始位置下标, 结束位置下标)
# 同样包前不包后
name = '3.1415926'
print(f".出现了", name.count('.'), f"次")

# 1.2 判断
# 1.2.1 startswith:是否以某个字符串开头，是的话返回True，不是返回False，如果设置开始和结束位置下标，则在指定范围内查找判断
# startswith(子字符串, 开始位置下标, 结束位置下标)
st = 'six star'
err = st.startswith('s')
if err == True:
    print("True")

# 1.2.2 endswith:是否以某个字符串结尾，是的话返回True，不是返回False，如果设置开始和结束位置下标，则在指定范围内查找判断
# 1.2.3 isupper:检测字符串中所有的字母是否都为大写，是的话返回True，不是返回False，如果设置开始和结束位置下标，则在指定范围内查找判断
st = 'six star'
print(st.isupper())
print('SIX'.isupper())
# 1.2.3 islower:检测字符串中所有的字母是否都为小写，是的话返回True，不是返回False，如果设置开始和结束位置下标，则在指定范围内查找判断

# 1.3 修改元素
# 1.3.1 replace():替换
# replace(旧内容, 新内容, 替换次数)
name = '好好学习天天向上'
print(name.replace('好', '牛'))
print(name.replace('好', '牛', 1))

# 1.3.2 split:指定分割符来切割字符串
st = 'hello,python'
print(st.split(','))  #['hello', 'python']以列表的形式进行返回
# 如果字符串中不包含分割内容，就不进行分割，会作为一个整体返回
print(st.split('1'))
print(st.split('o', 1)) #['hell', ',python']指定之分割一次

# 1.3.3 capitalize：第一个字符大写,其他都小写
st = 'heLlo'
print(st.capitalize())

# 1.3.4 lower:大写字母转为小写
st = 'HellO'
print(st.lower())

# 1.3.5 upper:小写字母转为大写
st = 'hello'
print(st.upper())