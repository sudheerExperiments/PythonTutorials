'''
Created on Jan 4, 2016

@author: tcsshvr
'''

#Returns words after splitting in a sentence
def break_words(stuff):
    words=stuff.split(' ')
    return(words)

#Returns words after sorting words in a word array
def sort_words(words):
    return(sorted(words))

#Returns first word in a words array
def print_first_word(words):
    #pop(0) returns first word in a array
    word=words.pop(0)
    return(word)

#Returns last word in a words array
def print_last_word(words):
    #pop(-1) returns last word in a array
    word=words.pop(-1)
    return(word)

#Returns a array of words after sorting them
def sort_sentence(sentence):
    words=break_words(sentence)
    return(sort_words(words))

#Returns first and last word in a sentence without sorting 
def print_first_and_last(sentence):
    words=break_words(sentence)
    first=print_first_word(words)
    last=print_last_word(words)
    return(first,last)

#Returns first and last word in a sentence after sorting 
def print_first_and_last_words_sorted(sentence):
    words=sort_sentence(sentence)
    first=print_first_word(words)
    last=print_last_word(words)
    return(first,last)

    
    
    
