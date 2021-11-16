#!/bin/bash

bandit_pass=`cat /etc/bandit_pass/bandit24`

mkdir -p /tmp/b24

echo $bandit_pass > /tmp/b24/pass
chmod -c -R 777 /tmp/b24
cat /etc/bandit_pass/bandit24 >>  /tmp/b24/pass
