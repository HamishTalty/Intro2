#!/usr/bin/env python3

def revLine(line):
    """Reverse the words in a line of text"""
    simpleLine = line.strip()
    words = simpleLine.split()
    revWords = reversed(words)
    newLine = ' '.join(revWords)
    return newLine

# Read lines of text from a file, reverse it and then write to output

from sys import exit

infile  = open("myFile", "r")
outfile = open("yourFile", "w")

line = infile.readline()

while line != '':  # '' is end of file

    newLine = revLine(line) + "\n" # Text needs "\n"
    
    try:
        outfile.write(newLine) 
    except:
        pass # Nowhere to write the error!
        # Tidy up before exit -- this could fail as well
        infile.close()
        outfile.close()
        exit(-1)
    
    line = infile.readline()

infile.close()
outfile.close()
