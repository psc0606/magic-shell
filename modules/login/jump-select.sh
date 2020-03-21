#!/usr/bin/env bash

# Read from a config file, the file has following csv format:
# username,ip,password
CONFIG_FILE=$1
if [ -r "$CONFIG_FILE" ]; then
  echo "Please select which ip to login:"
  # shellcheck disable=SC2006
  select ip in `awk -F, '{print $1 ":" $3}' "$CONFIG_FILE"`
  do
    echo "You selected ${ip}";
    # get ip string after `:`
    line=`grep "${ip#*:}" "$CONFIG_FILE"`
    # shellcheck disable=SC2206
    arr=(${line//,/ })
    # jum-ssh-password is the symbol link to jump-ssh-password.sh in PATH
    # shellcheck disable=SC2068
    jump-ssh-password ${arr[@]:1}
  done
else
  echo "The config file not exists."
fi
