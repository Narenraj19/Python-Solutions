'''
Name : Narendra Raj RK
Setno: 3
Question_no:9 
Description:Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
'''

def is_sorted(str):

    str2=[]

    for i in str:

        str2.append(i)

    str2.sort()

    if str2==str:

        print("True")

    else:

        print("False")

       
 
str=list(raw_input("Enter the List values:"))

is_sorted(str)