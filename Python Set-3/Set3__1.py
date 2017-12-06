'''
Name : Narendra Raj RK
Setno: 3
Question_no:1 
Description:A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string. 
            Use this idiom to write a one-line version of is_palindrome
'''

1)
def is_palindrome(str):
    str2=str[::-1]
    if str==str2:
        print("It is a Palindrome") 
    else:
        print("Not a Palindrome")

str=raw_input("Enter a string::")
print is_palindrome(str)
'''