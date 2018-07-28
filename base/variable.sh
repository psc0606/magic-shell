#!/bin/bash

##################################################
# 算术运算
##################################################
# shell处理都是按照string处理, 处理算术比较麻烦
var=1
var=${var}+1
# 打印1+1字符串, 而不是相加
echo "not sum:" ${var}

# shell算术运算，不推荐
no1=4
no2=5;
let res1=no1+no2
res2=$[no1+no2]
res3=$((no1+no2))
echo "sum:" ${res1} ${res2} ${res3}


## declare声明变量, 推荐
#
# declare -i 声明整数
declare -i n
n=10/3
echo "integer:" ${n}

# 声明数组
declare -a array
# shell的数组真变态, 其他语言都是[]，()表示元组, {}表示字典
# 没有逗号
array=(1 2 3 4 5 6 7)
echo "idx0,id1:" ${array[0]}, ${array[1]}
# 访问所有元素
echo "all:" ${array[*]}
# 获取数组长度
echo "array: "${#array[*]}
# 获取数组索引
echo "index:" ${!array[*]}

declare -a array2
array2[0]="a1"
array2[1]="a2"
array2[2]=0
echo ${array2[*]}


# 声明只读变量
declare -r readonly

# 声明函数
declare -f
