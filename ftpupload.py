#!/usr/bin/env python
########## python ftpupload.py

import ftplib
import sys

serverAddr = '217.182.200.111'
userName = 'user543116521'
passWD = 'Dap8K7shQbIx23a'
fileToUpload = sys.argv[1]
print("opening ftp...")
i = 1
while True:
    try:
        print('connecting ftp://217.182.200.111 - try ' + str(i))
        ftp217 = ftplib.FTP('217.182.200.111', userName, passWD, timeout = 10 )
        print(ftp217)
        break
    except:
        i += 1
print("changing directory...")
ftp217.cwd('mass_result')
print("directory changed succesfully...")
i = 0
while True:
    try:
        print("opening file " + fileToUpload)
        f = open(fileToUpload, 'rb')
        print("sending file to ftp...")
        ftp217.storbinary("STOR "+ fileToUpload, f)
        print("closing ftp connection ...")
        ftp217.quit()
        break
    except:
        print("faled to upload %s to ftp" % fileToUpload)
        i += 1
        print("this is try nomber %s, will try again now..." % str(i))
        # input("press Enter key to continue...")