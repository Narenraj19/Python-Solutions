'''
Name : Narendra Raj RK
Setno: 3
Question_no:8 
Description:Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). 
'''


def is_abecedarian(str):

    str2=[]

    for i in str:

        str2.append(i)

    str2.sort()

    if str==str2:

        print("True")

    else:

        print("False")


str=list(raw_input("Enter a String or a Number:"))

is_abecedarian(str)
    