'''
Created on Jun 19, 2014

@author: susanha
'''
import unittest
import Factor


class Test(unittest.TestCase):


    def testprimeFactors(self):
        self.assertEqual(Factor.primeFactorsOf(1),[])
        self.assertEqual(Factor.primeFactorsOf(2), [2])
        self.assertEqual(Factor.primeFactorsOf(3), [3])
        self.assertEqual(Factor.primeFactorsOf(4), [2,2])
        self.assertEqual(Factor.primeFactorsOf(5), [5])
        self.assertEqual(Factor.primeFactorsOf(6),[2,3])
        self.assertEqual(Factor.primeFactorsOf(7), [7])
        self.assertEqual(Factor.primeFactorsOf(8), [2,2,2])
        self.assertEqual(Factor.primeFactorsOf(9), [3,3])
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testprimeFactors']
    unittest.main()