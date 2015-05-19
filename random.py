#This code is about generating random numbers from 1 to 26.
import random
import re, string
x=random.randint(1,26)  # now x stores random number from 1 to 26
#take the input of string which u want to encrypt! 
print "\nEnter the string you want to encrypt." #Only letters a-z allowed(lowercase)!
encrypt_string = raw_input("\n: > ")
#Table below does mapping randomly
table = string.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[x:]+string.ascii_lowercase[:x])

print "Your encrypted code -  " + string.translate(encrypt_string,table)
