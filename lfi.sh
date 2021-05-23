#!/bin/bash
dir="/var/www/html/program";
for line in `cat /var/www/html/waf/txt/danger_list_lfi`
do
	echo `grep -nr $line $dir` >> /var/www/html/waf/txt/lfi.txt
done
