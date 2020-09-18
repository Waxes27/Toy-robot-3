#!/bin/bash

read -p "Name of FILE...(.py): " files
read -p "Unittest file e.g.(tests/test_main.py)" tests

while true; do
	python3 $files
	sleep 1.7
	clear
	#while true; do
		#python3 -m unittest $tests
		#sleep 10
		#clear
done
done
