#-------------------------------------------------------------------------
#--- config.py
#--- This program has variables and constants used globally.
#

from datetime import datetime
import os
import csv

#-------------------------------------------------------------------------
#---Variable declarations
filepaths = []

# Set to true to turn on print statements
Debug = False
#-------------------------------------------------------------------------
#--- Set up paths
#--- current directory path
myPyParagraphPath = os.getcwd()
print("myPyParagraphPath is ", myPyParagraphPath)
print()

#--- Absolute path of the output directory
outputPath = os.path.abspath("output")
print("outputPath is ",outputPath)
print()

#--- Absolute path of the data directory
dataPath = os.path.abspath("data")
print("dataPath is ",dataPath)
print()

#--- list contents of ouput directory
# List directory contents of output using absolute path
if Debug:
    print("Directory contents of output is ",os.listdir(os.path.abspath(outputPath)))
    print()

#--- List contents of data directory
# List directory contents of output using absolute path
if Debug:
    print("Directory contents of data is ",os.listdir(os.path.abspath(dataPath)))
    print()

#--- List all *.txt files in output directory
if Debug:
    for file in os.listdir(outputPath):
        if file.endswith(".txt"):
            print(outputPath + "\\" + file)
    print()

# List all *.txt files in the data directory
# and append to filepaths for processing.
for file in os.listdir(dataPath):
    if file.endswith(".txt"):
        filepaths.append(dataPath + "\\" + file)
        if Debug:
            print(dataPath + "\\" + file)

if Debug:
    print("filepaths is ", filepaths)
    print()