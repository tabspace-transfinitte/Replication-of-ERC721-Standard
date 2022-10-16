#!/usr/bin/bash

#argument 1 is name of nft
#Argument 2 us name of collection being added to
#argument 3 is url

wget $3
name=$(echo $3 | awk -F / '{print $NF}')
file=$(pwd)
cid=$(ipfs add $file/$name | awk '{print $2}')
touch $2.csv
line=$(cat $2.csv | wc -l)
if [ $line == 0 ];
then
	echo "1, ipfs://$cid" > $2.csv
else
	arr=($(awk '{print $1}' $2.csv| grep -o .))
        echo "$((${arr[0]} + 1)), ipfs://$cid" > $2.csv
fi
tznft create-nft-meta $1 alice ipfs://$cid
tznft set-pinata-keys 241a1732e2915550c91f 70aed7b980f11a49405c8f07d137f2522b12bcfe2a077f16e03ec34d85731acd --force
tznft pin-file $1.json --tag $1
tznft mint-from-file alice $2 --token_file $2.csv
echo "ipfs://$cid" >> $2.txt
