#!/usr/bin/env python
########## python ftpupload.py

from ftplib import FTP
import sys

serverAddr = '217.182.200.111'
userName = 'user543116152'
passWD = 'Dap8K7shQbIx28q'
fileToUpload = sys.argv[1]
print("opening ftp...")
ftp = FTP('217.182.200.111', userName, passWD)
print("ftp.dir()")
print("changing directory...")
ftp.cwd('mass_result')
print("directory changed succesfully...")
try:
    print("opening file " + fileToUpload)
    f = open(fileToUpload, 'r')
    print("sending file to ftp...")
    ftp.storlines("STOR "+ fileToUpload, f)
    print("closing ftp connection ...")
    ftp.quit()
except:
    print("faled to upload %s to ftp" % fileToUpload)