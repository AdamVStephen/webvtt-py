#!/usr/bin/bash
for f in *.vtt
do 
	python3 ./test.py "$f" | \
		while read line
			 do echo "$f : $line"
			 done
		 done | \
grep -v Contrib | grep -v "\*\*\*"
