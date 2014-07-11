'''
Created on Jul 10, 2014

@author: susanha
'''

import subprocess
import Transformations

def readGitFile(fileName):
    ## subprocess.call("git log -p -m > logfile")
    myList = []
    gitFile = open(fileName)
    myTrans = Transformations.Trans()
    for line in gitFile:
        myLine = line.strip()

        if myLine.find("Initial") > -1:
            myList.append(myTrans.NEWFILE)
        if myLine.find("+ pass") > -1:
            myList.append(myTrans.NULL)
    gitFile.close()
    return myList