'''
Created on Jan 4, 2016

@author: tcsshvr
'''

#Import ex25_1 where the function implementation is written(library is imported)
import ex25_MorePractice_1

sentence="I am working on python right now It seems pretty mind boggling"

#Splits and prints words in a sentence
words=ex25_MorePractice_1.break_words(sentence)
print("Words after split: %s" % words)

#Sorts the words in a word array
words_sorted=ex25_MorePractice_1.sort_words(words)
print("Words after sorting: %s" % words_sorted)

#Prints first word in a array of words
words1=ex25_MorePractice_1.print_first_word(words)
print("First word: %s" % words1)

#Prints last word in a array of words
words2=ex25_MorePractice_1.print_last_word(words)
print("last word: %s" % words2)

#Sorts a sentence and returns array of words
words=ex25_MorePractice_1.sort_sentence(sentence)
print("Words after sorting: %s" % words)

#Prints first and last word in a sentence without sorting
word1,word2=ex25_MorePractice_1.print_first_and_last(sentence)
print("First and last words without sorting: %s, %s" % (word1,word2))

#Prints first and last word in a sentence after sorting
word1,word2=ex25_MorePractice_1.print_first_and_last_words_sorted(sentence)
print("First and last words after sorting: %s, %s" % (word1,word2))