#!/bin/env python3.7
# coding=utf-8

"""
Author: peng.shaocheng
Time: 2017-12-03
Comment: jar conflict check, run it only in local
"""
import os
import sys
import readline
from modules.interactive import HistoryCompleter


def tip():
    print("##################################################################")
    print("#          Java jar冲突 Exception: ")
    print("# 类型一:")
    print("#     1. java.lang.ClassNotFoundException ")
    print("#     2. java.lang.NoSuchMethodError")
    print("#     3. java.lang.NoSuchFieldError ")
    print("# 类型二:")
    print("#     1. java.lang.NoClassDefFoundError ")
    print("# 类型三:")
    print("#     3. java.lang.LinkageError")
    print("#     2. java.lang.IncompatibleClassChangeError ")
    print("#")
    print("# 类型一错误是没有引入相应的jar包或者class冲突")
    print("# 类型二错误是class冲突")
    print("# 类型三错误是class冲突, 会导致该subclass的子类或实现类异常")
    print("# JAVA classpath是多路径,把classpath中所有jar包拷贝至一个目录中")
    print("#")
    print("#          请输入JAVA jar所在目录")
    print("##################################################################")


def check_jar(cp):
    if not os.path.exists(cp):
        print("路径不存在")
        return
    # 切换至当前工作目录
    os.chdir(cp)

    # 读取所有文件
    file_names = os.listdir(cp)
    class_dict = {}
    print("扫描jar包...")
    for fn in file_names:
        # 过滤非jar包
        if not fn.endswith('.jar'):
            continue
        print(fn)
        # 读取jar包中文件
        try:
            lines = os.popen('jar -tvf ' + fn).readlines()
        except KeyboardInterrupt:
            print("jar包扫描已被中止")
            sys.exit(1)
        for line in lines:
            tmp = line.split(' ')
            # 取class名
            class_name = tmp[-1].strip().replace('/', '.')
            # print class_name
            # 过滤掉非class文件
            if not class_name.endswith('.class'):
                continue
            if class_name in class_dict:
                jar_list = class_dict.get(class_name)
                jar_list.append(fn)
            else:
                # 空表
                jar_list = list()
                jar_list.append(fn)
            class_dict[class_name] = jar_list

    print("共扫描%d个jar包, 共%d个class文件".format(len(file_names), len(class_dict)))
    num = 0
    for (k, v) in class_dict.items():
        if len(v) == 1:
            # 没有jar包冲突
            continue
        print("{}==>".format(v))
        num += 1
    print("很有可能存在的冲突class文件个数: %d".format(num))


if __name__ == '__main__':
    tip()
    HistoryCompleter().loop_input(check_jar)
