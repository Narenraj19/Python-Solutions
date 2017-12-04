'''
Name : Narendra Raj RK
Setno: 1
Question_no:4b
Description:Find the time taken to go home 
'''


from __future__ import division
try:
  start=6.52
  t=start*60
  easy=2
  tempo=3
  total_time=((easy*(8/15))+(tempo*(7/12)))*60
  time=float((total_time+start)/60)
  print time
except Exception as e:
  print e