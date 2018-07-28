#! /bin/bash

# 匹配整个单词是否在词典中
# grep正则表达式, -q静默输出

word=$1
grep "^$1$" /usr/share/dict/american-english -q
if [ $? -eq 0 ]; then
    # ${word}比$word更直观, 不会把字符串混合一起, eg: ${word}string, $wordstring
	echo ${word} is a dictionary word;
else
	echo ${word} is not a dictorynary word;
fi
