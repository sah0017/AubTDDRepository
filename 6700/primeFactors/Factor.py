'''
Created on Jun 20, 2014

@author: susanha
'''



def primeFactorsOf(myInteger):
    myFactors = []
    if myInteger > 1:
        if (myInteger % 2) == 0:
            myFactors.append(2)
            myInteger = myInteger / 2
    if myInteger > 1:
        myFactors.append(myInteger)
    return myFactors

    