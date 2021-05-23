#!/bin/bash
dir="/home/david/text";
for line in `cat danger_list_rce1`
do
	echo `grep -nr $line $dir` >> rce1
done
