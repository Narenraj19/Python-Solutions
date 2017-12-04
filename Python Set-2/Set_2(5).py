'''
Name : Narendra Raj RK
Setno: 2
Question_no:5
Description:Sum of digits in a String
'''
try:
  def sumDigits(a):
    sum=0
    for i in s:
      if(i.isdigit()):
        sum=sum+int(i)
    print "sum is "+str(sum)
  a=raw_input("enter a string")
  sumDigits(a)
except Exception as e:
  print e  