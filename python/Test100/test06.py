#encoding: utf-8
# 斐波那契数列。
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

def fib(n):   # 查看斐波那契数列第n个斐波那契数
    if n == 1 or n == 2:
        return 1
    fibNum = fib(n-1) + fib(n-2)
    return fibNum

def fib2(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fibList(n): # 查看n个长度的斐波那契数列
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    List = [1,1]
    for i in range(3,n+1):
        num = fib(i)
        List.append(num)
    return List

def fibList2(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    List = [1,1]
    for i in range(2,n):
        List.append(List[-1]+List[-2])
    return List

print(fib(10))
print(fib2(10))

print(fibList(10))

print(fibList2(10))