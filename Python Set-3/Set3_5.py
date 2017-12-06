'''
Name : Narendra Raj RK
Setno: 3
Question_no:5 
Description:Write a function named avoids that takes a word and a string of forbidden letters, and that returns
            True if the word doesn’t use any of the forbidden letters.
'''


def avoids(str,list):
    if len(set(str) & set(list))!=0:
        return False
    else:
        return True
        
str=list(raw_input("string"))
list=list(raw_input("forbidden"))
print avoids(str,list)
