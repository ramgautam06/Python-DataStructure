# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:56:16 2020

@author: rgautam

This class prints the sum of two numbers

"""

class example1:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 
        
    def sum(self):
        total = self.num1 + self.num2
        return total 
    
def main():
    print("Starting Class")
    exe = example1(10 , 7) #exe is an object 
    print("The sum of numbers is " + str(exe.sum()))
    
if __name__ == '__main__':
    main()