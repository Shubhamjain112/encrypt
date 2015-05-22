#This code is about generating random numbers from 1 to 26.
import random
import re, string
x=random.randint(1,26)  # now x stores random number from 1 to 26
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

i=1
while i==1:
    print "Enter your choice"
    print "1.Encryption"
    print "2.Decryption"
    c=int(raw_input())
    if c==1:
        encryption()
    elif c==2 :
        decryption()
    else :
        print "Wrong choice"
    print "Do you want to continue : "
    choice=raw_input()
    if choice !="yes":
        i=2


