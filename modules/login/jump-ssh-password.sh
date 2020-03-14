#!/usr/bin/env bash

# I think use sshpass is more simple than expect.
# So you should install sshpass first, please google how to install sshpass in differernt os.

USER=$1
BASTION=$2
PWD=$3
CMD="ssh ${USER}@${BASTION} -o ServerAliveInterval=60 -o StrictHostKeyChecking=no"
sshpass -p $PWD $CMD