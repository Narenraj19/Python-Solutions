'''
Name : Narendra Raj RK
Setno: 3
Question_no:10 
Description:Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function
            called is_anagram that takes two strings and returns True if they are anagrams.

'''

def is_anagram(str1,str2):
    x=len(str1)
    y=len(str2)
    if x==y:
        a=str1.sort()
        #print a
        b=str2.sort()
        #print b
        if a==b:
            print("It is an anagram")
        else:
            print("It is not an anagram")
    else:
        print("The two strings are of different length")

str1=list(raw_input("Enter string1::"))
str2=list(raw_input("Enter String 2::"))
is_anagram(str1,str2)
'''
        