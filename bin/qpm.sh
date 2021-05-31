# shellcheck disable=SC2034
#20210524
DATE=$1
echo "$DATE"
FORMAT_DATE=$(date -d "$DATE" +'%Y-%m-%d')
echo "$FORMAT_DATE"
max_count=0
max_rq=0
max_time=""
for i in {0..1439} ; do
    minute=$(date -d "+$i min $DATE" +'%Y-%m-%d %H:%M')
    echo "$minute"
    line=$(cat info.log."${FORMAT_DATE}"-* | grep "$minute" | grep "ExecutionTimeInterceptor:262" | awk -F'=' 'BEGIN{c=0}{c+=$3}END{print c, NR}')
    echo "$line"
    # split string into array, this is the prefer way.
    IFS=' ' read -ra arr <<< "$line"
    count="${arr[0]}"
    rq="${arr[1]}"
    echo "$count"
    echo "$rq"
    # [ $max_count -lt $count ] && max_count=$count
    # [ $max_rq -lt $rq ] && max_rq=$rq
    if [ $max_count -lt $count ];then
      max_count=$count
      max_rq=$rq
      max_time=$minute
    fi
done
echo "峰值:"
echo "$max_time"
echo "$max_count"
echo "$max_rq"