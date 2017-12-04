'''
Name : Narendra Raj RK
Setno: 1
Question_no:5
Description:power and sqrt 
'''

from __future__ import division
import math
try:
  num=int(raw_input("enter value: "))
  sq=math.sqrt(num)
  pwr=num/sq
  if((pwr>0)&(pwr<6)):
    if((math.pow(sq,pwr))==num):
      print "square root: " +str(sq)
      print "power: " +str(pwr)
    else:
      print "the number is not equal"
  else:
    print "not in the range"
except Exception as e:
  print e