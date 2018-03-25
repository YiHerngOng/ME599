#!/usr/bin/env python

#Yi Herng Ong   Lab 4
#SID 932278854

import sys
import string
from time import time


def open_file_to_list(filename):
    words = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                words.extend(line.strip().split())
    except:
        sys.exit(str(filename)+ " "+ "does not exist")

    return words

def decapitalize(list_):
    decap_list = []
    for i in xrange(len(list_)):
        decap_list.append(list_[i].lower())

    return decap_list

def word_count(list_):
    return len(list_)


def check_argument():
    usr_argv = sys.argv[1:]
    if len(usr_argv) < 2:
        sys.exit("Number of Arguments must be 2") #system exit if argument less than 2
    return usr_argv

def num_words_both_files(wnp_text, words_text):
    count = 0
    words_text_set = set(words_text)
    for i,x in enumerate(wnp_text):
        if x in words_text_set:
            count += 1
    return count

def clean_punctuation(wnp_text, words_text):
    new_wnp_text = []
    table = string.maketrans("","")
    for x in xrange(len(wnp_text)):
        str = wnp_text[x].translate(table, string.punctuation)
        new_wnp_text.append(str)

    new_words_text = []
    for y in xrange(len(words_text)):
        str_ = words_text[y].translate(table, string.punctuation)
        new_words_text.append(str_)

    return new_wnp_text, new_words_text

def check_unique_words(list_):
    list_set = set()
    for i in xrange(len(list_)):
        if list_[i] not in list_set:
            list_set.add(list_[i])
    return len(list_set)

def check_words_not_in_other(text1, text2):
    text2_set = set(text2)
    text1_set = set(text1)
    return len(text1_set - text2_set)

#Make sure not to count word twice in one file while matching with the other
def check_words_in_both(text1, text2):
    text2_set = set(text2)
    text1_set = set(text1)
    return len(text2_set & text1_set)


if __name__ == '__main__':
    start = time()
#   Lab Direction 1 & 2
#   Check arguments, open files and count words
    usr_argv = check_argument()
    wnp_text = open_file_to_list(usr_argv[0])
    words_text = open_file_to_list(usr_argv[1])

#   Lab Direction 3
#   Print number of unique words
#   Clean punctuation
    new_wnp_text = []
    new_words_text = []
    new_wnp_text, new_words_text = clean_punctuation(wnp_text, words_text)

#   Decapitalize (make them case-insensitive)
    decap_wnp_text = []
    decap_words_texts = []
    decap_wnp_text = decapitalize(new_wnp_text)
    decap_words_text = decapitalize(new_words_text)

#   Calculate unique words in each file
    unq_wnp_count = check_unique_words(decap_wnp_text)
    unq_words_count = check_unique_words(decap_words_text)

#   Lab Direction 4
#   Calculate number of words exist only in wnp, in words, in both
    only_wnp = check_words_not_in_other(decap_wnp_text,decap_words_text)
    only_words = check_words_not_in_other(decap_words_text, decap_wnp_text)
    count_in_both = check_words_in_both(decap_wnp_text, decap_words_text)

#   Printing results
    print usr_argv[0], ":\n", " ", word_count(wnp_text), "words\n", "  Unique:", str(unq_wnp_count)
    print usr_argv[1], ":\n", " ", word_count(words_text), "words\n", "  Unique:", str(unq_words_count)
    print "Only", usr_argv[0], ":", only_wnp, "\n", "Only", usr_argv[1], ":", only_words, "\n", "Both files: ", count_in_both

#   Time spent to run the entire code
    end = time()
    print "Time used : ", str(end - start), " ", "seconds"