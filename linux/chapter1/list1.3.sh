#!/usr/bin/env bash

UNAME="uname -a"
printf "Gathering system information with the $UNAME command: \n\n"
$UNAME

DISKSPACE="df -h"
printf "Gathering diskspace information with the $DISKSPACE command: \n\n"
$DISKSPACE