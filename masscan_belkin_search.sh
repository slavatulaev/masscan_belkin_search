#!/bin/bash
# the parametr should be a filename with ip ranges to scan
IP_address=''
username=''
password=''

iptables -A INPUT -p tcp --dport 61111 -j DROP

while IFS='' read -r line || [[ -n "$line" ]]; do
    # echo "IP read from file: $line"
    masscan $line -p80,443 --banners --source-port 61111 -oG mass_raw_res.txt --max-rate 10000
    grep -f banners.txt mass_raw_res.txt | grep -o -E '([0-9]{1,3}[\.]){3}[0-9]{1,3}' | sort | uniq > ${line////-}.txt
    ./ftpupload.py ${line////-}.txt
    rm ${line////-}.txt

done < "$1"
