'''
Created on Jul 10, 2014

@author: susanha
'''

import subprocess

def readGitFile(fileName):
    ## subprocess.call("git log -p -m > logfile")
    gitFile = open(fileName)
    myString = gitFile.read()
    gitFile.close()
    return myString