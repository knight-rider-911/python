#!/bin/bash

SCRIPT_NAME=$1
LOG_NAME='/var/log/acess.log'

find /var/log/nginx/  -type f -ctime +7 -exec tar -cvfz archive.tar.gz /var/log/nginx  {} + | tee log-$(date +%y%m%d)
error_log=`cat $LOG_NAME | grep 500 | wc -l| tee log-$(date +%y%m%d)`