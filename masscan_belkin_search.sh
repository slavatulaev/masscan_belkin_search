#!/bin/bash
# the parametr should be a filename with ip ranges to scan

iptables -A INPUT -p tcp --dport 61112 -j DROP

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Current IP range: $line"
    # remove leading whitespace characters
    trimmedLine="${line#"${line%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    trimmedLine="${trimmedLine%"${trimmedLine##*[![:space:]]}"}"   
    outFile=${trimmedLine////-}.txt
    echo "Output to file $outFile"
    masscan $line -p80,443 --banners --source-port 61112 -oG mass_raw_res.txt --max-rate 10000
    echo "Finished scanning... now performing grep..."
    grep -f banners.txt mass_raw_res.txt | grep -o -E '([0-9]{1,3}[\.]){3}[0-9]{1,3}' | sort | uniq > $outFile
    echo "grep IPs to $outFile done. Now sendint it to FTP..."
    ./ftpupload.py $outFile
    echo "File $outFile uploaded to ftp server. Time to delete it..."
    rm $outFile
    echo "File $outFile sucsessfully deleted"
    echo "End of current cycle. Going Next..."
done < "$1"
