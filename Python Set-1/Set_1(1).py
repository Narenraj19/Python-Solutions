'''
Name : Narendra Raj RK
Setno: 1
Question_no:1
Description:Finding the largest odd numbers
'''


a=raw_input("Enter no1:")

b=raw_input("enter no2 ")

c=raw_input("enter no3:")

d=int(a)

g=int(b)

f=int(c)

if(d%2>0) and d > g  and g > f:

    try:

        print("The Greatest is no1")

    except Exception as e:

        print(e)

if(g%2>0) and g>f and f>d:

    try:

        print("The Greatest is no2")

    except Exception as e:

        print(e)

if(f%2>0) and f>g and g>d:

    try:

        print("The Greatest is no3")

    except Exception as e:

        print(e)


else:

    print("Entered nos are Even!!! ")
