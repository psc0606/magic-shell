#!/bin/bash

# 命令行运行
# 提取其中的ID,feed number,time cost,total time cost, 并根据time cost筛选

# 日志格式
# 2019-11-29 11:20:59,877 INFO [rank] recommend for 745537529 with feed number 21, model ab:test-rec:1.4.3, time cost 4ms, recommend total time cost 19ms
# 2019-11-29 11:20:59,878 INFO [rank] recommend for 603603999 with feed number 355, model ab:test-rec:1.4.3, time cost 21ms, recommend total time cost 20ms

tail -F rank.log | grep "recommend for" | awk -F',' '{split($2, arr, " ");split($4, brr, " ");split($5, crr, " ");time_cost=substr(brr[3],0,length(brr[3])-2)+0;total_time_cost=substr(crr[5], 0,length(crr[5])-2)+0;if(time_cost>10)printf "%s\t%d\t%s\t%s\n",arr[6],arr[10],time_cost,total_time_cost}'