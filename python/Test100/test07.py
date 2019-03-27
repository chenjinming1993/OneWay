#encoding: utf-8
# 将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。

a = [5,6,2,7,9]
b = a[:]
print(b)

# a=[1,2,3,4,5]，b=a和b=a[:]，有区别么？
# 你调用下
# b.append(6)
# print (a, b)
# 就看出区别了:
#     前者传递引用
#     后者是拷贝

# test 区别

c = a
b.append(7)
print(a,'\n',b)
c.append(6)
print(a,'\n',b,'\n',c)