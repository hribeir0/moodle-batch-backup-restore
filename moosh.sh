#!/bin/bash
echo "Argument 1: $1"
cd /var/www/html/moodledev
moosh -n $1 $2
echo "Argument 2: $2"