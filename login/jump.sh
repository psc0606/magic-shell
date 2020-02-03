#!/usr/bin/env bash

# 功能: 快速登录跳板机 or 线上机器
# 特性：
#   1. 快速登录跳板机 or 线上机器
#	2. 支持keep alive不掉线
#	3. 支持ip/docker实例名/域名登录
# 作者：peng.shaocheng
# 时间: 2018.05.16
# 更新: 2018.12.29
# 使用: 放于本地 or 环境变量
# 示例：
#   1. 不带参数直接登录跳板机
#      jump.sh
#   2. 通过IP登录docker实例
# 	   jump.sh 10.220.2.18
#   3. 使用docker名登录
# 	   jump.sh ces-xxx-service-test-master-51c3ded-tfnkm
#      jump.sh ces-xxx-service-test-master-51c3ded-tfnkm.k8s

# 登录用户名，替换成自己的
user="peng.shaocheng"

# 生成谷歌验证码, python脚本替换成自己的路径
# 通过python获取google验证码
# fixme
google_code=`python2.7 /Users/path/dev-tools/google_code.py`

# 跳板机
bastion='gw.abc.com'

bastion_cmd="ssh ${user}@${bastion} -o ServerAliveInterval=60 -o StrictHostKeyChecking=no -p 16020"
bastion_cmd_tt=${bastion_cmd}" -tt"

# 探测跳板机是否需要谷歌验证码
expect -c "
    spawn -noecho ${bastion_cmd} pwd > /dev/null
    set timeout 1
    expect {
        \"MOMO google auth*\" { send \"${google_code}\n\"; }
        eof {send_tty \"\";exit}
    }
    interact
" &> /dev/null
#    expect eof

#IP地址简单校验
is_valid_ip_format()
{
    if [[ "$1" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] ;then
        return 0
    else
        return 1
    fi
}

#欢迎界面
hello()
{
echo '
     .=""=.
    / _  _ \
   |  d  b  |
   \   /\   /
  ,/"-=\/=-"\,
 / /        \ \
| /  Hello   \ |
\/ \        / \/
    ".    ."
    _|`~~`|_
    /|\  /|\
'
echo -e 'WELCOME '${user}''

echo '
示例：
  1. 不带参数直接登录跳板机
     jump.sh
  2. 通过IP登录docker实例
	 jump.sh 10.220.2.18
  3. 使用docker名登录
	 jump.sh ces-xxx-service-test-master-51c3ded-tfnkm
     jump.sh ces-xxx-service-test-master-51c3ded-tfnkm.k8s
'
}

# 无参时直接登录跳板机
if [[ $# -ne 1 ]];then
    ${bastion_cmd}
    exit
fi

# 判断是使用docker名/IP登录
USER='user1'

is_valid_ip_format $1
is_ip_host=$?
if [[ ${is_ip_host} -eq 0 ]];then
	#如果参数为IP地址
	hello
    ${bastion_cmd_tt} ssh ${USER}@$1
else
	#判断 .k8s结尾, 目前docker全部都是以.k8s结尾的实例名
	end_with_k8s=`echo $1 | grep "\.k8s"`
	suffix=""
	if [[ -z "$end_with_k8s" ]]; then
		suffix=".k8s"
	fi

	#nslookup反向解析ip
	ns=`${bastion_cmd} nslookup $1${suffix}`

	#r=`echo "$ns" | grep "Non-authoritative answer:"`
	suc=`echo "$ns" | sed -n '4p'`
	# 匹配是否存在该字符串，存在认为解析成功
	if [[ ${ns} =~ 'Non-authoritative answer:' ]];then
		#调用hello函数
		hello
		#字符串剪切到末尾
		domain=`echo "$ns" | sed -n '5p' | cut -c 6-`
		echo "Domain:" ${domain}
		ip=`echo "$ns" | sed -n '6p' | cut -c 10-`
		echo "IP:    " ${ip}
		${bastion_cmd_tt} ssh ${USER}@${ip}
	else
        echo "docker实例名无法解析"
	fi
fi
