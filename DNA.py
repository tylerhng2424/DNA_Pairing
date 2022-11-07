
# -------------------------------------------------------------------
# File name: DNA.py
#
#   Program Description:
#       This program reads a DNA sequence given by the inputted text file
#    and allows for the user to select and change the specific nucleobase they would want
#    replaced.
#       In addition, the program counts the number of each nucleobase in the DNA sequence
#    while also allowing the user to reset the sequence if they wish to.
#
# Version: 2.8
# Author: Tyler Ng
#
# References:
# https://www.pythonforbiologists.org/
# https://www.jetbrains.com/help/pycharm/opening-and-reopening-files-in-the-editor.html
# https://docs.python.org/3/library/stdtypes.html?#truth-value-testing
# ------------------------------------------------------------------
# Importing re module
import re

# Asks user to select base
# Assigns base selection to s
print("Input the nucleobase you would like to replace:")
s = input()
search_text = s

# Asks user for base replacement
# Assigns replacement base to r
print("Now input the nucleobase you would like to replace the original:")
r = input()
replace_text = r

# Creating a function to
# replace the text
def fixSequence(search_text, replace_text):
    # Opening the file in read and write mode
    with open('gene.txt', 'r+') as f:
        # Reading the file data and store
        # it in a file variable
        # ALso removing white spaces
        file = f.read().replace(" ","")
        print("Original Sequence:")
        print(file)
        sequence_length = range(len(file))
        # Replacing the pattern with the string
        # in the file data
        file = re.sub(search_text, replace_text, file)

        # Setting the position to the top
        # of the page to insert data
        f.seek(0)

        # Writing replaced data in the file
        f.write(file)
        print("Replace Sequence:")
        print(file)
        # Truncating the file size
        f.truncate()

        # Counts specific characters in sequence
        numA = file.count("A")
        numT = file.count("T")
        numC = file.count("C")
        numG = file.count("G")

        # Displays character count
        print('A: ', numA)
        print('T: ', numT)
        print('C: ', numC)
        print('G: ', numG)

    # Return "Text replaced" string
    return "Text replaced"

# Assigning fixSequence function to finalSequence
# Calling/Printing final sequence
finalSequence = fixSequence(search_text, replace_text)
print(finalSequence)

# Resets edited sequence to original
print("Input 'R' to reset Sequence, input any key to quit:")
x = input()
if (x == 'R'):
    fixSequence(replace_text, search_text)