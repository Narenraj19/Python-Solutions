'''
Name : Narendra Raj RK
Setno: 2
Question_no:6
Description:def findAnEven(l):
	    """Assumes l is a list of integers
	    Returns the first even number in l
	    Raises ValueError if l does not contain an even number"""
'''

def findAnEven(l): 

    for i in l: 

        if int(i) % 2 == 0: 

            return i 

    raise ValueError("No even numbers in list!") 




a=raw_input("enter numbers")

l=[]

for i in a:

    l.append(i)
print  l

c=findAnEven(l)

print c