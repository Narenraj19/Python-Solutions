'''
Name : Narendra Raj RK
Setno: 1
Question_no:4b
Description:To Find the wholesale cost of books purchased 
'''


from __future__ import division
try:
  def cost():
    a=0
    cp=24.95
    d=40
    sp=3
    sp1=0.75
    n=int(raw_input("enter number of copies: "))
    if(n==1):
      a=a+cp*(d/100)*sp
    else:
      a=a+(cp*(d/100)*sp1*n)
    print "the wholesale cost is " + str(a)
  cost()
except Exception as e:
  print e