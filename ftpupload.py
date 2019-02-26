#!/usr/bin/env python
########## python ftpupload.py

from ftplib import FTP
import sys

serverAddr = '217.182.200.111'
userName = 'user543116152'
passWD = 'Dap8K7shQbIx28q'
fileToUpload = sys.argv[1]

ftp = FTP('217.182.200.111', userName, passWD)
# print(ftp.dir())
ftp.cwd('mass_result')
f = open(fileToUpload, 'r')
ftp.storlines("STOR "+ fileToUpload, f)
ftp.quit()