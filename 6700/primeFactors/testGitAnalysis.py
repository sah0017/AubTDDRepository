'''
Created on Jul 10, 2014

@author: susanha
'''
import unittest
import GitFile


class Test(unittest.TestCase):


    def testGitFile1(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\testFile1.txt"),"first")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGitFile1']
    unittest.main()