#!/bin/bash

# Simple bash script to login
# You can change this script as your need.

USER:=$1
HOST:=$2
ssh ${USER}@${HOST} -o ServerAliveInterval=60 -o StrictHostKeyChecking=no -p 3313