# main.py
#
# PyBoss: input files - employee_data1.csv, employee_data2.csv.
# Run these files separately because the records aren't unique.
#
# The program can process multiple employee files if they have
# unique records.  Any files processed will be written to one
# output file.
#
# Steps:
# 1) Read the .csv files into a python list
#   * Starting column titles: Emp ID, Name, DOB, SSN, State
#   * After column titles: Emp ID, fName, lName, DOB, SSN, State
#
# 2) Convert the loaded data:
#   a) Name should be split into first and last name columns
#   b) DOB should be written as mm/dd/yyyy
#   c) SSN should be written as ***-**-9999
#   d) State should be abbreviated see:
# https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
# 3) output results to console
# 4) output results to a .csv file called updated_employees.csv

import os
import csv

# config2.py process to call definePaths() doesn't work!
#from config2 import definePaths

# Configuration file for standard code
import config as cfg

# State table contained in stateAbbreviations.py
from stateAbbreviations import us_state_abbrev

# for a file datetime stamp
from datetime import datetime

# # Test import of us_state_abbrev Dictionary
# print(us_state_abbrev['California'])
# print()
#-------------------------------------------------------------------------
#--- Variable declarations
filepaths = []
employee_data1 = []

Debug = False
#-------------------------------------------------------------------------
#--- Functions
def readCSVFile(files,employeeList):
    if Debug:
        print("In readCSVFile...")
        print()
    # Read the .csv file into a list
    for file in files:
        # Save values into path
        path = file
        if Debug:
            print("path - file is ",file)
            print()

        count = 0

        # Use path to save the drive, path and filename
        drive, path = os.path.splitdrive(path)
        path, filename = os.path.split(path)
        if Debug:
            print('Drive is %s, Path is %s and file is %s' % (drive, path, filename))
            print()

        with open(file) as csvfile:
            print("Reading CSV File...", file)
            print()
            # Use csv.Reader to read data into a list from a csv file.
            csvReader = csv.reader(csvfile, delimiter=',')
            for row in csvReader:
                employeeList.append(row)
                count += 1
            csvfile.close()
        if Debug:
            print("Rows processed: ", count)
            print()
    return employeeList

def writeCSVFile(output_file, employeeList):
    # Write out the file after updates to columns
    output_path = os.path.join(cfg.outputPath, output_file)
    if Debug:
        print("output_path is ", output_path)
        print()

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in employeeList:
            csvwriter.writerow(i)

def splitName(empList):
    # Emp ID, Name, DOB, SSN, State
    name = empList[1]
    if Debug:
        print("emp list name is ", name)
        print()
    fName,lName = name.split(' ')
    empList.insert(1, fName)
    empList.insert(2, lName)
    empList.remove(name)
    return empList

def changeDateFormat(empList):
    # Emp ID, FName, LName, DOB, SSN, State
    empBDate = empList[3]
    if Debug:
        print("emp list date is ", empBDate)
        print()
    newBDate = datetime.strptime(empBDate,"%Y-%m-%d").strftime("%m/%d/%Y")
    empList.insert(3, newBDate)
    empList.remove(empBDate)
    return empList

def obfuscateSSN(empList):
    # Emp ID, FName, LName, DOB, SSN, State
    oldSSN = empList[4]
    a,b,c = oldSSN.split("-")
    if Debug:
        print("a is %s, b is %s, c is %s " % (a,b,c))
        print()
    newSSN = "***-**-" + c
    empList.insert(4,newSSN)
    empList.remove(oldSSN)
    return empList

def abbrevState(empList):
    # Emp ID, FName, LName, DOB, SSN, State
    State = empList[5]
    StateAbbrev = us_state_abbrev[State]
    if Debug:
        print("State abbreviation is ", StateAbbrev)
        print()
    empList.insert(5,StateAbbrev)
    empList.remove(State)
    return empList

#-------------------------------------------------------------------------
#--- print statements for testing import module
if Debug:
    print("output file name is ", cfg.output_file)
    print("myPyBossPath is ", cfg.myPyBossPath)
    print("outputPath is ", cfg.outputPath)
    print("dataPath is ", cfg.dataPath)
    print("filepaths is ", cfg.filepaths)
    print()

#-------------------------------------------------------------------------
#--- main body

# Call function to read the .csv file into a list
employee_data1 = readCSVFile(cfg.filepaths,employee_data1)
print("Finished reading .csv file...")
print()

#-------------------------------------------------------------------------
#--- Update columns
for i in range(1,len(employee_data1)):
    lst1,lst2,lst3,lst4 = [],[],[],[]

    lst1 = splitName(employee_data1[i])
    lst2 = changeDateFormat(lst1)
    lst3 = obfuscateSSN(lst2)
    lst4 = abbrevState(lst3)
    employee_data1.insert(i,lst4)
    del employee_data1[i+1]
    if Debug:
        print("employee list is ", employee_data1)
        print()
    
#-------------------------------------------------------------------------
#--- Call function to write and print out the file
writeCSVFile(cfg.output_file, employee_data1)
print("Finished writing out .csv file...")
print()

# print the files processed
print("Files processed: ")
print("----------------")
for i in cfg.filepaths:
    print(i)
print()

# print the file to standard output
print("CSV file contents: ")
print("==================")
for i in range(1, len(employee_data1)):
    print(", ".join(employee_data1[i]))






