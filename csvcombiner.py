'''
PMG Coing Assessment: CSV - Combiner
Author: Philip Wang
File Name: csvcombiner.py
Description: This is a Python program. CSV combiner will take several CSV files as arguments. 
    Each CSV file will have the same columns. 
    The output of this program is a new CSV file that 
    includes the rows from each of the inputs as well as an additional column 
    that lists the filename from which each row came
    (It only contains the file's base name not the file path). 
    Use filename as the header for the additional column.
'''
# Use pandas to merge files and convert csv to dataframe. 
# DataFrame is a 2 dimensional, size-mutable, potentially heterogeneous tabular data. 
# This module, sys, provides access to variables used or maintained by the interpreter. 
# We used 'sys.argv' to pass values to the script.
# OS provides a portable way of using operating system dependent functionality. 
# We mainly used os to manipulate paths.   
import pandas as pd 
import sys 
import os 

# Input is filePath and it's a string. Output is fileName, also a string. 
# It takes the filePath as the input and uses the rfind() method finds the last occurence of '/'.
# indexName is an integer and it's the index of the last '/'. 
# Then we can get the fileName using filePath[indexName+1].
# Then assign the value to fileName.
def findFileName(filePath):
    # Return the remainder of the string after finding the last '/' (filename)
    indexName = filePath.rfind('/')
    fileName = filePath[indexName+1:]
    return fileName

# This function has two inputs dataFrame and csvFiles, and returns the ouput dataFrame. 
# dataFrame is a Data Frame and csvFiles is a list contains file names. 
# In this function, we will loop through the csv files 
# Use .read_csv() method to read comma-separated values into dataframe. 
# Lastly, use pd.concat() method to concatenate new dataframe and the old one. 
def mergeFilesTog(dataFrame, csvFiles):
    # going through the remaining csv files in a for loop
    for i in range(1, len(csvFiles)):
        # creating new dataframe
        dataFrame1 = pd.read_csv(csvFiles[i])
        # Including file name and giving the appropriate name using FindFileName
        dataFrame1['filename'] = findFileName(csvFiles[i])
        # For all of the files, merge the new dataframe with the original ones. 
        dataFrame = pd.concat([dataFrame,dataFrame1])
       
    return dataFrame

# In this function, we will return dataFrame and csvFiles. 
# dataFrame is a DataFrame type and csvFiles is a list that contains csv files.
# We will first loop through the list of command line arguments passed to a Python script.
# Use os.path.isfile() to check if the specified path exists or not. 
# Next, use read_csv() method to read csv file into dataFrame. 
def preProcess():
    csvFiles = []
    # Looping over files that were specified as commnd line arguments
    for i in range(1,len(sys.argv)):
        # Looping through, and append those values when the path exists.
        if os.path.isfile(sys.argv[i]):
            # '-4' indicates the file extension and check if it's .csv. 
            if sys.argv[i][-4:] == '.csv': 
                csvFiles.append(sys.argv[i])
    # Access the CSV and read them into dataframe by using .read_csv() method. 
    dataFrame = pd.read_csv(csvFiles[0])
    return dataFrame, csvFiles

# In this main function, we first call preProcess() function to get variable dataFrame and csvFiles.
# Then calling findFileName function to retrieve the name and put it into dataFrame. 
# Then, merge files together by calling mergeFilesTog function if num of csvFiles is more than 1.
# Use set_index() method to set index of a dataframe.  
# Lastly, use to_csv() method to write object to newCsvFile and print it. 
def main():
    dataFrame, csvFiles = preProcess()
    # Including the name in the filename column and get the names from csvFiles. 
    dataFrame['filename'] = findFileName(csvFiles[0])

    # When the number of csvFiles is more than one, merge files together. 
    # And dataFrame cannot be empty. Otherwise, an error will occur "list index out of range". 
    if len(csvFiles) > 1:
        # give it to the original dataframe
        dataFrame = mergeFilesTog(dataFrame, csvFiles)

    # set the index as the first column using .set_index from Pandas library (email_hash)
    dataFrame = dataFrame.set_index(dataFrame.columns[0])
    
    # The new csv will convert dataframe to a csv file
    # Print it as script
    newCsvFile = dataFrame.to_csv()
    print(newCsvFile)

if __name__ == "__main__":
    main()