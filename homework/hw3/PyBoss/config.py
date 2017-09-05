# config.py
#
from datetime import datetime
import os

filepaths = []

Debug = False

#--- output file name with datetime stamp
date_string = datetime.now().strftime("%d%b%Y%H%M%S")
output_file = "emp_data" + date_string + ".csv"
if Debug:
    print("output file name is " + output_file)
    print()

#--- Set up paths
# current directory path
myPyBossPath = os.getcwd()
print("myPyBossPath is ", myPyBossPath)
print()

# Absolute path of the output directory
outputPath = os.path.abspath("output")
print("outputPath is ",outputPath)
print()

# Absolute path of the data directory
dataPath = os.path.abspath("data")
print("dataPath is ",dataPath)
print()

#--- list contents of directories
# List directory contents of output
if Debug:
    print("Contents of output is ",os.listdir(os.path.abspath(outputPath)))
    print()

# List directory contents of data
if Debug:
    print("Contents of data is ",os.listdir(os.path.abspath(dataPath)))
    print()

# Find all *.csv files in output directory
for file in os.listdir(outputPath):
    if file.endswith(".csv"):
        print(outputPath + "\\" + file)
print()

# Find all *.csv files in the data directory
# and append to filepaths.
for file in os.listdir(dataPath):
    if file.endswith(".csv"):
        if Debug:
            print("dataPath: " + dataPath + "\\" + file)
            print()
        filepaths.append(dataPath + "\\" + file)
if Debug:
    print("My filepaths is ", filepaths)
    print()