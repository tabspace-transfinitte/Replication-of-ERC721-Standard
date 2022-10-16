#!/usr/bin/bash

#1st argument is name of collection

tznft create-collection-meta $1
tznft create-collection alice --meta_file $1.json --alias $1
touch $1.txt
