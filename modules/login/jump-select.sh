#!/usr/bin/env bash

# This is simple login select menu. It read from a config file, the file has following csv format:
# username,ip,password,defalt_remote_cmd
#
# Usage:
#     First you should config the csv file with format as above.
#     Second, use like this:
#     jump-select.sh <path_to_config> [-x]

CONFIG_FILE=$1
# Debug on, f set to -x, or debug off.
DEBUG_X=$2
if [ -r "$CONFIG_FILE" ]; then
  echo "Please select which ip to login:"
  # shellcheck disable=SC2006
  select ip in `awk -F, '{print $1 ":" $3}' "$CONFIG_FILE"`
  do
    [[ "$DEBUG_X" = "-x" ]] && set -x
    echo "You selected ${ip}";
    # get ip string after `:`
    line=`grep "${ip#*:}" "$CONFIG_FILE"`
    # shellcheck disable=SC2206
    arr=(${line//,/ })
    PWD="${arr[3]}"
    USER="${arr[1]}"
    IP="${arr[2]}"
    # shellcheck disable=SC2124
    REMOTE_CMD="${arr[@]:4}"
    CMD="sshpass -p '$PWD' ssh -t -o ServerAliveInterval=60 -o StrictHostKeyChecking=no ${USER}@${IP} '${REMOTE_CMD}; bash'"
    [[ "$DEBUG_X" = "-v" ]] && set +x
    # Only use eval to execute, eval will replact the variable.
    eval $CMD
  done
else
  echo "The config file not exists."
fi
