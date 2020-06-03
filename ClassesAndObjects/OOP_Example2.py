# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:18:01 2020

@author: rgautam

Input:
    - Sentence or string 

Output:
    - number of words in the string
    - number of words of given length (eg. 2 letter words)
    - number of words starting with given letter (e.g. 'a' )
    
"""
from string import punctuation 

class Letters:
    #the constructor will take the word and divide into words 
    def __init__(self, sen):
        for p in punctuation:
            sen = sen.replace(p, " ")
        
        sen = sen.lower()
        #print(sen)
        
        #defining varaibles for this class 
        self.words = sen.split()
    
    def number_of_words(self):
        return (len(self.words))
    
    def given_length_words(self, num):
        count = 0 
        for x in self.words:
            if len(x) == int(num): #type casting to integer
                count = count + 1
        return count
    
    def given_letter_words(self, t):
        count = 0
        for w in self.words:
            if(w[0] == 't'):
                count = count + 1
        return count 

def main():
    #ask for user input 
    sentence = input("Enter the senetnce you want to analyze:  ")
    
    #creating letter object
    analyze = Letters(sentence)
    print(analyze.words)
    print("The number of words are: ", analyze.number_of_words())
    
    length = input("Enter the length of word you want to check:  ")
    print ("The number of ",length, "letter words is  ", analyze.given_length_words(length))
    
    letter = input("Enter the starting letter :  ")
    print ("The number of words starting with '",letter, "' is  ", analyze.given_letter_words(letter))
    
if __name__ == "__main__":
    main()