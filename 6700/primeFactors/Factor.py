'''
Created on Jun 20, 2014

@author: susanha
'''



def primeFactorsOf(myInteger):
    myFactors = []
    index = 2
    while myInteger > 1:
        while (myInteger % index) == 0:
            myFactors.append(index)
            myInteger = myInteger / index
        index = index + 1
    
    return myFactors

    