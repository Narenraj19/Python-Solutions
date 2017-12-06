'''
Name : Narendra Raj RK
Setno: 3
Question_no:7 
Description: Write a function named using_only() that takes a word and a string of letters, and that
             returns True if the word contains only letters in the list
'''


def using_only(word,string):
    for i in word:
        if i not in string:
            return "false"
    return "true"        
            
word=raw_input("enter word: ")
string=list(raw_input("enter string of letters: "))
a=using_only(word,string)
print(a)