'''
Name : Narendra Raj RK
Setno: 2
Question_no:2 
Description:A number, a, is a power of b if it is divisible by b and a/b is a power of b.
            Write a function called is_power that takes parameters a and b 
            and returns True if a is a power of b
'''

try:
  def is_power(a,b):
    d=a/b
    if(a%b==0 and d%b==0):
      print "true"
    else:
      print "false"
      
  a=int(raw_input("enter A value: "))
  b=int(raw_input("enter B value: "))
  is_power(a,b)
except Exception as e:
  print e

