'''
Name : Narendra Raj RK
Setno: 3
Question_no:2 
Description:Write a function called rotate_word() that takes a string and an integer as parameters, 
            and that returns a new string that contains the letters from the original string "rotated" by the given amount.
'''
2)
def rotate_word(s,n):
    a=[]
    b=[]
    c=[]
    for i in s:
        a.append(ord(i))
    #print a
    for i in a:
        b.append(i+n)    
    #print b
    for i in b:
        c.append(chr(i))
    print c   

s=list(raw_input("Enter The word"))
n=int(raw_input("Enter the no by which u want to rotate:"))
rotate_word(s,n)
'''