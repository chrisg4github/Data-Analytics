#-------------------------------------------------------------------------
#--- main.py
#
# PyParagraph: 
# input files - paragraph1.txt, 
#               paragraph2.txt, 
#               TKMB_Paragraph1.txt, 
#               TKMB_Paragraph2.txt
#
# 1) Assess the passage for each of the following:
#    a) Approximate word count
#    b) Approximate sentence count
#    c) Average letter count (per word)
#    d) Average sentence length (in words)
#
# 2) output results to console
#
# 3) output results to a .txt file 
#    
#    Sample File and Console Output:
#    Paragraph Analysis
#    ==================
#    File processed: paragraph1.txt
#    Approximate Word Count: 122
#    Approximate Sentence Count: 5
#    Average Letter Count (per word): 4.56557377049
#    Average Sentence Length (in words): 24.4
#
# For more information on regular expressions, go to
# https://en.wikipedia.org/wiki/Regular_expression
#
#-------------------------------------------------------------------------
import os
import re
import string
import csv

# Configuration file
import config as cfg

# class Paragraph
import classParagraph as cp

# datetime module
from datetime import datetime

#-------------------------------------------------------------------------
#--- Variable declarations
Debug = False

#-------------------------------------------------------------------------
#--- Function declarations

#-------------------------------------------------------------------------
#--- Print statements for import config as cfg
if Debug:
    print("myPyParagraphPath is ", cfg.myPyParagraphPath)
    print("outputPath is ", cfg.outputPath)
    print("dataPath is ", cfg.dataPath)
    print("filepaths is ", cfg.filepaths)
    print()

#-------------------------------------------------------------------------
#--- Main body


#--- For loop to process each data file (paragraph)
for file in cfg.filepaths:
    fileList, sentenceList, sentenceWordList, resultsList  = [], [], [], []
    sentenceCounter, wordCounter, lettersPerWord = 0, 0,0
    paragraphName = ""

    path, fName = os.path.split(file)
    paragraphName = fName.strip(".txt")

    # Create a Paragraph object
    paragraphName = cp.Paragraph(fName, "data")
    # Describe Paragraph object
    print(paragraphName.describeFile())

    # Append file processed to results file
    resultsList.append("File processed: " + fName)

    # Create a unique output_file name for each paragraph file
    fName = fName.strip(".txt")
    date_string = datetime.now().strftime("%d%b%Y%H%M%S")
    output_file = fName + "_" + date_string + ".txt"

    #--- Read entire file into a list
    # Read the entire file and return a list
    fileList = paragraphName.readTextFile(file)

    # Read the file line by line - return a list
    #fileList = paragraph1.readFile(file)

    #--- Analize each paragraph
    #--- Sentence count
    sentenceList, sentenceCounter = paragraphName.sentenceCount(fileList)
    resultsList.append("Approximate Sentence Count: " + str(sentenceCounter))

    # --- Word count
    sentenceWordList, wordCounter = paragraphName.wordCount(sentenceList)
    resultsList.append("Approximate Word Count: " + str(wordCounter))

    #--- Average letter count per word
    lettersPerWord = paragraphName.avgLetterCount(wordCounter, sentenceWordList)
    resultsList.append("Average Letter Count (per word): {:.2f}".format(lettersPerWord))

    #--- Average sentence length in words
    resultsList = paragraphName.avgSentenceLength(wordCounter, sentenceCounter, resultsList)

    # --- Write out results to a output_file
    paragraphName.writeFile(output_file, cfg.outputPath, resultsList)

    #--- Write results to the console
    paragraphName.writeToConsole(resultsList)

#--- Print final messages to the console
print("All done!")



