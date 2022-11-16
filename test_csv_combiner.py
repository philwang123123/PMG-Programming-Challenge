'''
Author: Philip Wang
Description: Several unit test for testing csvcombiner.py
'''

import unittest
import pandas as pd
from csvcombiner import findFileName, mergeFilesTog, main

class csvCombinerUnitTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.csv = "random.csv"
        self.path = "~/Home/Desktop/file1/file2/existing.csv"

    def tearDown(self):
        print("TEARDOWN Called...")
        self.csv = ''
        self.path =''
        

    # Testing the file with the extension .csv whether it's a csv file or not. 
    def testFileExtension(self):
        print("TEST - 1 Called...\n")
        self.assertEqual(self.csv[-4:],'.csv', "Not a csv file")
    
    # Compare the two file names and check if they are equal. 
    def testNameAreEqual(self):
        print("TEST - 2 Called...\n")
        self.assertEqual(findFileName(self.path), 'existing.csv', "File name is wrong!!")
    
    # Test if two files' name are the same, and the error should be AssertionError.      
    def testNonExistingFile(self):
        print("TEST - 3 Called...\n")
        with self.assertRaises(AssertionError):
            result = findFileName(self.path)
            self.assertEqual(result, "nonexisting.csv")
      
    # Input is "Home/Desktop/philip.pdf", it will pass.    
    def testFileNameWithRegularPath(self):
        print("TEST - 4 Called...\n")
        filePath = "Home/Desktop/philip.pdf"
        result = findFileName(filePath)
        self.assertEqual(result, "philip.pdf")        
    
    # Input is "Home/Desktop/File1/File2/File3/books.csv", it will pass.
    def testFileNameWithLongPath(self):
        print("TEST - 5 Called...\n")
        filePath = "Home/Desktop/File1/File2/File3/books.csv"
        result = findFileName(filePath)
        self.assertEqual(result, "books.csv")
    
    # Input is "Home/computers.csv", it wil pass.
    def testFileNameWithShortPath(self):
        print("TEST - 6 Called...\n")
        filePath = "Home/computers.csv"
        result = findFileName(filePath)
        self.assertEqual(result, "computers.csv")
    
    # Inputs are csvFiles and dataFrame. I set both to lists which will give us a typeerror. 
    def testMergeFilesTogExpectTypeError(self):
        print("TEST - 7 Called...\n")
        with self.assertRaises(TypeError):
            csvFiles = ["fixtures/clothing.csv", "fixtures/accessories.csv"]
            dataFrame = ["fixtures/clothing.csv, fixtures/accessories.csv"]
            result = mergeFilesTog(dataFrame, csvFiles)
            self.assertEqual(result, dataFrame)
    
    # Inputs are csvFiles and dataFrame, I set csvFiles as a list 
    # Use .DataFrame() method to set it to dataframe. And this will give us a value error.
    def testMergeFilesTogExpectValueError(self):
        print("TEST - 8 Called...\n")
        with self.assertRaises(ValueError):    
            csvFiles = ["fixtures/accessories.csv", "fixtures/clothing.csv"]
            dataFrame = pd.DataFrame(csvFiles)
            result = mergeFilesTog(dataFrame, csvFiles)
            self.assertEqual(result, dataFrame.to_string())
            
    # Test if the dimension is correct and dataFrame is not empty. 
    def testMergedFileDimension(self):
        print("TEST - 9 Called...\n")
        csvFiles = ["fixtures/accessories.csv", "fixtures/clothing.csv", "fixtures/household_cleaners.csv"]
        dataFrame = pd.DataFrame(csvFiles)
        result = dataFrame.shape
        self.assertEqual(result, (3,1))
    
    # Test if there is no file and dataFrame should be (0,0)    
    def testMergedFileIfEmpty(self):
        print("TEST - 10 Called...\n")
        csvFiles = [ ]
        dataFrame = pd.DataFrame(csvFiles)
        result = dataFrame.shape
        self.assertEqual(result, (0,0))
        
    # Test if there are several files from different paths
    def testMultipleMergedFiles(self):
        print("TEST - 11 Called...\n")
        csvFiles = ["Desktop/File1/cellphones.csv", "computers.csv", "books.csv", "fixtures/accessories.csv", "fixtures/clothing.csv", "fixtures/household_cleaners.csv"]
        dataFrame = pd.DataFrame(csvFiles)
        result = dataFrame.shape
        self.assertEqual(result, (6,1))
            
    
            
 
        
        
                
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
