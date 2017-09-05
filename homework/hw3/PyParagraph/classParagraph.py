#-------------------------------------------------------------------------
#--- classParagraph.py
#
#-------------------------------------------------------------------------
#--- Read in a paragraph and output the following
#    a) Approximate word count
#    b) Approximate sentence count
#    c) Approximate letter count (per word)
#    d) Average sentence length (in words)
#
#-------------------------------------------------------------------------

import os
import csv
import re
import string

# Configuration file
import config as cfg

# datetime module
from datetime import datetime

Debug = False
#-------------------------------------------------------------------------
# --- Class declarations
class Paragraph:

    def __init__(self, fileName, fileDir="data"):
        self.fileName = fileName
        self.fileDir = fileDir
        if Debug:
            print("Created Paragraph object!")


    def describeFile(self):
        print()
        return (
            f"Paragraph Object Description\n"
            f"============================\n"
            f"File Name: {self.fileName}\n"
            f"File Directory: {self.fileDir}\n"
        )


    def wordCount(self, sList):
        sWList = []
        wCount = 0
        for i in sList:
            sWList.append(i.split())
        if Debug:
            print("Sentence Word List is ", sWList)

        #Count the words in each sentence
        for i in sWList:
            wCount = wCount + len(i)
            if Debug:
                print("Sentence word count is ", len(i))
                print("Total Word count: ", wCount)
                print()
        return sWList, wCount

    def sentenceCount(self, fList):
        sList = []
        sentenceCount = 0
        se_break = re.compile("[.!?] \s+ ", re.VERBOSE)
        for i in range(0, len(fList)):
            sList = (se_break.split(re.sub('[ï»¿,]', '', fList[i])))
        sCount = len(sList)
        if Debug:
            print("Number of Sentences is ", sCount)
            for i in sList:
                print("sList is ", i)
            print()
        return sList, sCount


    def avgLetterCount(self, wCounter, sWList):
        lCounter = 0
        lPWord = 0
        for i in sWList:
            for j in i:
                if Debug:
                    print(i)
                lCounter += len(j)
                if Debug:
                    print(j)
            if Debug:
                print("countLetters total: ", lCounter)
        lPWord = lCounter / wCounter
        if Debug:
            print("Average Letter Count (per word): {:.2f}".format(lPWord))
        return lPWord


    def avgSentenceLength(self, wCount, sCount, rList):
        rList.append("Average words per Sentence: {:.1f}".format(wCount/sCount))
        return rList

    # Read each line of a file
    def readFile(self, fileName):
        fList = []
        filepath = fileName
        fh = open(filepath, 'r')
        # Iterate, read, and append line by line
        for line in fh:
            if Debug:
                print(line)
            fList.append(line)
        fh.close()
        return fList

    # Reads entire file
    def readTextFile(self, fileName):
        path, file = os.path.split(fileName)
        fList = []
        filepath = fileName
        with open(filepath, 'r') as fh:
            lines = fh.read()
            if Debug:
                print(lines)
            fList.append(lines)
        fh.close()
        return fList

    def writeFile(self, outputFile, outputPath, rList):
        rList.insert(0,"Paragraph Analysis Results")
        rList.insert(1,"==========================")
        rList.append("\n")
        rList.append("PyParagraph program analysis completed...")

        filepath = os.path.join(outputPath, outputFile)
        fh = open(filepath, 'w')
        # Iterate, and write line by line
        for line in rList:
            if Debug:
                print(line)
            fh.write(line + '\n')
        fh.close()

    def writeToConsole(self, rList):
        # Iterate, and print line by line
        print()
        for line in rList:
            print("".join(line))
        print()
