'''
Created on Jul 10, 2014

@author: susanha
'''

import subprocess
import Transformations
import codecs

def readGitFile(fileName):
    ## subprocess.call("git log -p -m > logfile")
    myList = []
    gitFile = codecs.open(fileName, encoding='utf-16')
    myTrans = Transformations.Trans()
    for line in gitFile:
        if line[0] == '+':
            myList.append('New line')
        if line[0] == '-':
            myList.append('line removed')
        if line.find("Initial") > -1:
            myList.append(myTrans.NEWFILE)
        if line.find("pass") > -1:
            myList.append(myTrans.NULL)
    gitFile.close()
    return myList