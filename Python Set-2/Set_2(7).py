'''
Name : Narendra Raj RK
Setno: 2
Question_no:7
Description:Given String is a Palindrome or NoT
'''

def palindrome_check(s):  
    a=reversed(s)
    if(list(s)==list(a)):
        print "It is a palindrome"
    else:
        print "It is not a palindrome"

s=raw_input("Enter a string")
palindrome_check(s)
