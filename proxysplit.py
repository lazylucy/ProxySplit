#!/usr/bin/python3

import re
import sys


#get commandline arguments

try:
    inlist = open(sys.argv[1], "r")
    inlistlines = inlist.readlines()
    outlist = open(sys.argv[2], "a+")
    if sys.argv[3] == '1' or sys.argv[3] == '2': #check that export type is valid
        exptype = sys.argv[3]
        exptype = int(exptype)
    else:
        print("Not a valid export type(valid types are 1 for 'TYPE   xx.xxx.xx.x PORT' or 2 for 'type://xx.xxx.xx.x:port')")
        exit()

except:
    print("Command line error, make sure the command is written correctly.")
    exit()

#identify proxylist format

def proxyident():
    if bool(re.search('Proxy [A-Z][A-Z]',inlistlines[1])) == True:  #Example proxybroker list
        inlisttype = 3
    elif bool(re.search('(.*?)://(.*?):(.*?)',inlistlines[1])) == True: #Example http format list
        inlisttype = 2
    elif bool(re.search('(.*?)\t(.*?)\t(.*?)',inlistlines[1])) == True: #Example proxychains list
        inlisttype = 1
    else:
        print("Can't identify list type")
        exit()
    return inlisttype

#append to list based on type 

def appendtolist(i,et):
    if et == 1:
        outlist.write("{}\t{}\t{}\n".format(i[0],i[1],i[2]))
    elif et == 2:
        outlist.write("{}://{}:{}\n".format(i[0].lower(),i[1],i[2]))

#extract proxy type, ip, port and write it to file

def extractandwrite(inlisttype):
    if inlisttype == 3:
        for info in inlistlines:
            extracted = re.findall("\[(.*?)\] (.*?):(.*?)>",info)
            extractedob = extracted[0]
            appendtolist(extractedob,exptype)

    elif inlisttype == 2:
        for info in inlistlines:
            extracted = re.findall("(.*?)://(.*?):(.*?)$",info)
            extractedob = extracted[0]
            appendtolist(extractedob,exptype)

    elif inlisttype == 1:
        for info in inlistlines:
            extracted = re.findall("(.*?)\t(.*?)\t(.*?)$",info)
            extractedob = extracted[0]
            appendtolist(extractedob,exptype)

extractandwrite(proxyident())
