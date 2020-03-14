#!/bin/bash

# This script is used to test a process id exists or not.
# It will read a pid from a pid file, such as supervisord.pid etc

# Use process id not by process name, but you can also use process name
PID=`cat $1`
# echo $PID
# If the target id not exists, the result is 1 (including default title), or the its result is not 1.
IS_EXISTS=`ps -p $PID | wc -l`
if [ $IS_EXISTS -le 1 ];then
    # not exists
    exit 0
else
    # exists
    exit 1
fi

