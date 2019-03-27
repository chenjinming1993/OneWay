#encoding: utf-8
# 输出 9*9 乘法口诀表。

print('打印9*9 乘法口诀表')
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print('%d * %d = %d' % (j,i,i*j),end="  ")
    print()

# Python3中的print函数s输出后是默认换行，如果我们需要函数在输出以后不换行，那么需要在print函数后面加end=""