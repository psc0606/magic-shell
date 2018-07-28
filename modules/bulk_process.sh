#!/usr/bin/env bash
# 批量处理文件内容

declare -i i=1

#while [ $i -le 254 ];do

#   echo "192.168.1."$i >> gg
#   let i=$i+1

#done

filename="../log"
while read line;do
   echo ${line} >> ${filename}
   echo ${line}

   let i=$i+1
   if [ ${i} -eq 100 ];then
        let i=0
        echo "sleep..."
        sleep 2
    fi
done < Hug.log