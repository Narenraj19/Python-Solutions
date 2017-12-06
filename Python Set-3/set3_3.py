'''
Name : Narendra Raj RK
Setno: 3
Question_no:3 
Description:Write a function called has_no_e that returns True if the given word doesn’t have the letter "e" in it.
'''
3)
def has_no_e(str):
    if 'e' in str:
        print("False")
    elif 'E' in str:
        print("False")
    else:
        print("True")

str=raw_input("Enter a String:")
has_no_e(str)
'''