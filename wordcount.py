
import string
import sys

def word_count(filename): 

    """Counting the number of times a word appears in a file"""
    #Write a program, wordcount.py, that opens a file, and counts 
    #how many times each space-separated word occurs in that file. 
    #Your program should then print those counts to the screen.# put your code here.


    with open(filename) as input_file:
    #loop over filename
    #rstrip
    #split by " "
        word_count_dict = {}

        for line in input_file:
            line = line.rstrip()
            input_file_line = line.split(" ")
            #print input_file_line
            for word in input_file_line:
                word = word.lower()
                word = word.strip(string.punctuation)
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

        alphabetical_word_count = sorted(word_count_dict.items())

        for word, number in alphabetical_word_count:
            print "%s: %d" % (word, number)


                  

word_count(sys.argv[1])