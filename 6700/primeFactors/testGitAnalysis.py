'''
Created on Jul 10, 2014

@author: susanha
'''
import unittest
import GitFile
import Transformations

class Test(unittest.TestCase):

    def setUp(self):
        self.myTrans = Transformations.Trans()
    '''        
    def testGitFileInitial(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\testFile1.txt"),[self.myTrans.NEWFILE])

    def testGitFileInitialAndPass(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\testFile2.txt"),[self.myTrans.NEWFILE, self.myTrans.NULL])
    '''
    def testLargeGitFile(self):
        self.assertEqual(GitFile.readGitFile("c:\\Users\\susanha\\git\\6700test\\revLogFile-short"),['New line', 'line removed', self.myTrans.NULL,'New line'])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGitFile1']
    unittest.main()