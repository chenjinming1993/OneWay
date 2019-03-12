#encoding: utf-8
import os
command = 'print "www.baidu.com"'
r = os.popen(command)
info = r.readlines()
for line in info:
    line = line.strip('\r\n')
    print(line)