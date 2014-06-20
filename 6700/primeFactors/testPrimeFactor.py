'''
Created on Jun 19, 2014

@author: susanha
'''
import unittest
import Factor


class Test(unittest.TestCase):


    def testprimeFactors(self):
        self.assertEqual(Factor.primeFactorsOf(1),[])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testprimeFactors']
    unittest.main()