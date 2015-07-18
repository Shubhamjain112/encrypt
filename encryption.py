#This code is about generating random numbers from 1 to 25.
#Instead of generating random numbers from 1 to 26, only numbers from 1 to 25 have been generated to avoid..
#...THE 'unfortunate' case where no encryption takes place (the one corresponding to x = 26).
import random
import re, string
x=random.randint(1,25)  # now x stores random number from 1 to 25
#take the input of string which u want to encrypt!
def encryption():
    print "\nEnter the string you want to encrypt." #Only letters a-z allowed(lowercase)!
    encrypt_string = raw_input("\n: > ")
    #Table below does mapping randomly
    table = string.maketrans(
            string.ascii_lowercase,
            string.ascii_lowercase[x:]+string.ascii_lowercase[:x])

    print "Your encrypted code -  " + string.translate(encrypt_string,table)


def decryption():
    print "\nEnter the string you want to decrypt." #Only letters a-z allowed(lowercase)!
    decrypt_string=raw_input("\n: > ")
    table2=string.maketrans(string.ascii_lowercase,string.ascii_lowercase[26-x:]+string.ascii_lowercase[:26-x])

    print "Your decrypted code -  " + string.translate(decrypt_string,table2)

encryption()
decryption()


