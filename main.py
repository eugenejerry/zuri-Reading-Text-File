import string
import os.path

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


# Open “main.py”, and complete the function “read_file_content”. It should accept 
# a filename as an argument and read the text contained in that file. It should return a string.
####READING TEXT#################################################################
def read_file_content(filename):
    # [assignment] Add your code here
    with open('C:/Users/DELL/Desktop/ZURI DEV/zuri projects/Live class-Python/Reading-Text-Files/story.txt') as f:
        lines = f.read()
        print(lines)

        #lines = f.read()
        # print(lines)
read_file_content('C:/Users/DELL/Desktop/ZURI DEV/zuri projects/Live class-Python/Reading-Text-Files/story.txt')
# return "Hello World"


##############################################################################
#Complete the function “count_words”. It uses “read_file_content” to read the text contained in “story.txt”.
# It should return a dictionary whose keys are unique words, and their values the count of those words in the text e.g {“as”:10, “would”:5}.

def count_words():
    text = read_file_content('C:/Users/DELL/Desktop/ZURI DEV/zuri projects/Live class-Python/Reading-Text-Files/story.txt')
    mydictionary = {}
    for line in text:
        line = line.strip()
        line = line.lower()
        
        line = line.translate(line.maketrans("," "", string.puntuation))
        words = line.split()
        
        for word in words:
            if word in mydictionary:
                mydictionary[word] +=1
            else:
                mydictionary[word] = 1
                
    for key in list(mydictionary.keys()):
        print(f"{{\"{key}\": {mydictionary[key]}}}, ", end=" ")
count_words()

    #return {"as": 10, "would": 20}


# testing###################################################
