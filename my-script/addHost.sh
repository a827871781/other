#!/bin/bash
ip=$1
if [ ! ${ip} ]; then
    echo "ip is miss"
    exit 1
fi

if [ ! $2 ]; then
    name=$ip
fi
user=$3
port=$4
if [ ! $3 ]; then
    user='root'
fi
if [ ! $4 ]; then
    port='22'
fi
echo "Host ${name}" >>/Users/syz/.ssh/config
echo "  HostName ${ip}" >>/Users/syz/.ssh/config
echo "  User ${user}" >>/Users/syz/.ssh/config
echo "  Port ${port}" >>/Users/syz/.ssh/config
cd /Users/syz/.ssh
a='ssh-copy-id -i root@'
eval $a$ip





