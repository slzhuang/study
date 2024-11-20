age = 21

if age < 18:
    print('未成年不能上网')

score = int(input('请输入您的成绩: '))
if score < 60:
    print('不及格')
elif score == 100:
    print('满分')
elif score >= 60:
    print('及格')