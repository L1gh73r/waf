#!/bin/bash
dir="/home/david/text";
for line in `cat danger_list_rce2`
do
	echo `grep -nr $line $dir` >> rce2
done
