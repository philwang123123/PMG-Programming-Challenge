# PMG Programming Assessment Challenge
This is a Python program. CSV combiner will take several CSV files as arguments. Each CSV file will have the same columns. The output of this program is a new CSV file that includes the rows from each of the inputs as well as an additional column that lists the filename from which each row came(It only contains the file's base name not the file path). Use filename as the header for the additional column. 
CSV files are used to store data. They are sometimes useful for moving data between different systems. This program allows you to merge CSV files easily and quickly, it allows to concatenate multiple files in order to get a single one. If the data in the files changes, you can sync those changes to the master CSV file. No need to repeat any manual work. 

# Usage Limits:
1. No size limit
2. No limit to the number of CSV files

# Programming Language, Library, and Tools
• Python 3.10.8
• Pandas 1.5.1
• sys
• os

# Methods 
.rfind() It finds the last occurrence of the specified value.
pd.read_csv() It reads a csv file into dataframe.
pd.concat() Concatenate pandas objects. 
os.path.isfile It's used to check whether the specified path is an existing file or not. 
sys.argv[] The list of command line arguments passed to a Python script.
pd.read_csv() It reads a csv file into dataframe.
.set_index() It sets a dataframe(lists or series) as index of a dataframe.
.to_csv() It converts dataframe into csv data. 

# How to run this program
Through command line:
$ python csvcombiner.py fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv > output.csv
If your Python version is the latest:
$ python3 csvcombiner.py fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv > output.csv

Test this program:
python -m unittest test_csv_combiner.py
If your Python version is the latest:
$ python3 -m unittest test_csv_combiner.py

# Example output after running csvcombiner.py
Given two input files named clothing.csv and accessories.csv

clothing.csv:
email_hash	category
21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63	Shirts
21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63	Pants
166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b	Cardigans

accessories.csv:
email_hash	category
176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab	Wallets
63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe	Purses

This program would output
output.csv:
email_hash	category	filename
21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63	Shirts	clothing.csv
21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63	Pants	clothing.csv
166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b	Cardigans	clothing.csv
176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab	Wallets	accessories.csv
63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe	Purses	accessories.csv



