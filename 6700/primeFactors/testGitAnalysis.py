'''
Created on Jul 10, 2014

@author: susanha
'''
import unittest
import GitFile
import Transformations

class Test(unittest.TestCase):

    def setUp(self):
        myTrans = Transformations.Trans()
        
    def testGitFile1(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\testFile1.txt"),[0])

    def testGitFile2(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\testFile2.txt"),[0,1])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGitFile1']
    unittest.main()