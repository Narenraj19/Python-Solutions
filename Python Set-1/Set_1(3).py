
'''
Name : Narendra Raj RK
Setno: 1
Question_no:3
Description:To get 10 numbers and find the largest odd number 
'''




try:
  print "enter the numbers: "
  max=None
  for i in range(0,10):
    num=int(raw_input())
    for j in range(0,10):
      if(num%2!=0):
        if(num>max):
          max=num
  if(max is None):
    print "No odd number"
  print "largest odd number is "+str(max)
except Exception as e:
  print e