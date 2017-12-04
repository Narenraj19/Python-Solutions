Name : Narendra Raj RK
Setno: 2
Question_no:8
Description:The built-in function eval takes a string and evaluates it using the Python interpreter


import math
def eval_loop(n):
    e=eval('%s' % n)
    print e
    a=raw_input("Enter another expression or done if finished")
    if(a=='done'):
        print "The last result is ",e
    else:
        eval_loop(a)


n=raw_input("Enter the expression:")
eval_loop(n)