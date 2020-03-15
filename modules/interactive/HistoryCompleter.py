#!/bin/env python3
# coding=utf-8

import readline
import logging
import os
import sys
import rlcompleter
import atexit

"""
说明: 交互式输入自动补全器, 具有记忆历史输入和使用tab自动补全的功能, 模拟shell的功能
时间: 2017-12-03
示例1: 
    def echo:
        line = HistoryCompleter().get_input()
        print(line)
        
示例2:
    def echo2:
        HistoryCompleter().loop_input(handler)
        
    def handler(self, line):
        print(line)
"""
USER_HOME = os.environ['HOME']
LOG_FILENAME = USER_HOME + '/.completer.log'
HISTORY_FILENAME = USER_HOME + '/.completer.hist'

logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d thread: %(threadName)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )


class HistoryCompleter(object):
    def __init__(self):
        """
        实例创建时自动初始化
        """
        self.matches = []
        self.init()
        return

    def init(self):
        # 指定自动补全的分割符, 默认分割符较多，会包含导致/ . *无法补全
        readline.set_completer_delims('\n')
        # 注册completer
        readline.set_completer(self.complete)

        # 兼容不同平台的tab自动补全
        # mac平台为darwin, centOs为linux2, version_info均为2
        if sys.platform == 'darwin' and sys.version_info[0] == 2:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

        # 只应初始化一次
        if os.path.exists(HISTORY_FILENAME):
            readline.read_history_file(HISTORY_FILENAME)

    def get_history_items(self):
        """
        获取历史输入
        """
        # 列表解析语法
        # xrange in py2 equals range in py3
        history_items = [readline.get_history_item(i)
                         # for i in xrange(1, readline.get_current_history_length() + 1)
                         for i in range(1, readline.get_current_history_length() + 1)
                         ]
        return self.__remove_dup(history_items)

    @staticmethod
    def __remove_dup(list_items):
        """
        去掉列表中重复的元素
        """
        no_repeat_set = set()
        for item in list_items:
            if item in no_repeat_set:
                continue
            else:
                no_repeat_set.add(item)
        return list(no_repeat_set)

    def complete(self, text, state):
        """
        tab自动补全实现
        """
        response = None
        if state == 0:
            history_values = self.get_history_items()
            logging.info('history: %s', history_values)
            if text:
                self.matches = sorted(h
                                      for h in history_values
                                      if h and h.startswith(text))
            else:
                self.matches = []
            logging.info('matches: %s', self.matches)
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.info('complete(%s, %s) => %s', repr(text), state, repr(response))
        return response

    @staticmethod
    def get_input(prompt='>>> '):
        """
        python动态语言尽量少用@staticmethod, 没有静态编译初始化的概念
        获取标准输入
        """
        try:
            # python不支持do-while
            while True:
                # input() in py3 equals raw_input() in py2
                line = input(prompt).strip()
                # line = raw_input(prompt).strip()
                if line == '':
                    continue
                # 输入不为空break
                # return line
                break
        except KeyboardInterrupt:
            sys.exit(1)

        # 仅保留200条
        readline.set_history_length(200)
        atexit.register(readline.write_history_file, HISTORY_FILENAME)
        return line

    @staticmethod
    def loop_input(handler=None, prompt='>>> '):
        """
        循环处理, 设置处理函数
        """
        try:
            while True:
                # raw_input() in py2 equals input() in py3
                # line = raw_input(prompt).strip()
                line = input(prompt).strip()
                if line == '':
                    continue
                if line == 'quit' or line == 'exit':
                    print("Bye Bye~")
                    break
                if handler is None:
                    break
                handler(line)
        except KeyboardInterrupt:
            sys.exit(1)
        finally:
            readline.write_history_file(HISTORY_FILENAME)
