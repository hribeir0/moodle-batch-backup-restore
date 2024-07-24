#!/bin/bash
echo "Argument 1: $1"
cd /var/www/html/moodle401
moosh -n $1
#echo "Argument 2: $2"