#encoding: utf-8
# 输入某年某月某日，判断这一天是这一年的第几天？
print('year:')
year = int(input())
print('month:')
month = int(input())
print('day')
day = int(input())
print('输入时间为：',year,'年',month,'月',day,'日')
number = [0,31,59,90,120,151,181,212,243,273,304,334]
if month>0 and month<13:
    dayNum = number[month-1] + day
else:
    print('输入错误')
if year%4==0 and year%100!=0 or year%400==0:
    print('是闰年')
    if month>2:
        dayNum += 1
else:print('不是闰年')
print('输入时间为这一年的第',dayNum,'天')