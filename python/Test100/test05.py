#encoding: utf-8
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# print('请输入三个数：')
# x = int(input('请输入x：'))
# y = int(input('请输入y：'))
# z = int(input('请输入z：'))
# print('输入的三个数为：',x,y,z)

def type1():
    print('请输入三个数：')
    x = int(input('请输入x：'))
    y = int(input('请输入y：'))
    z = int(input('请输入z：'))
    print('输入的三个数为：', x, y, z)
    print('由小到大输出',sorted([x,y,z]))
    if x>y:
        n = x
        x = y
        y = n
    if x>z:
        print('由小到大输出',z,x,y)
    elif y>z:
        print('由小到大输出',x,z,y)
    else:
        print('由小到大输出',x,y,z)

def type2():
    print('请输入三个数：')
    x = int(input('请输入x：'))
    y = int(input('请输入y：'))
    z = int(input('请输入z：'))
    print('输入的三个数为：', x, y, z)
    print('由小到大输出',sorted([x,y,z]))

type1()
# type2()