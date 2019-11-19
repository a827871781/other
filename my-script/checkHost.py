#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
dict ={}
dictA ={}
def readFile(fileName):

    flag=0
    lastHost=""
    file = open(fileName)
    while 1:
        line = file.readline()
        if not line:
            break
        if flag:
            dict[lastHost.split( )[1]]=line.split( )[1]
            flag=0
        if "Host " in line:
            flag=1
            lastHost = line


def printDict():
    index=1
    for key in dict.keys():
        dictA[index]=key
        print('{} : {}'.format(index,key))
        index=index+1


if __name__ == '__main__':
    readFile("/Users/syz/.ssh/config")
    print("以下为当下所有可连接服务器:")
    printDict()
    print("输入 0 退出连接")
    print("请输入想要连接服务器的序号:")
    a = int(sys.stdin.readline().strip())
    if a==0:
        print("已结束")
    else:
        str="ssh root@{}".format(dict[dictA[a]])
        print(str)
        os.system(str)
