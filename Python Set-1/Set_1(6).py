'''
Name : Narendra Raj RK
Setno: 1
Question_no:6
Description:Find the sum of numbers separated by commas 
'''

try:
  s=raw_input("enter numbers: ")
  s.split(',')
  sum=0
  for i in s.split(','):
     sum=sum+float(i)
  print "sum of the numbers is "+str(sum)
except Exception as e:
  print e
