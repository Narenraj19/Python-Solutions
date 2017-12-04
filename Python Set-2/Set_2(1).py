'''
Name : Narendra Raj RK
Setno: 2
Question_no:1
Description:GCD of numbers 
'''


try:
  def gcd(no1,no2):
    if(no2==0):
      print "GCD is "+str(no1)
    elif((no1%no2)==0):
      print "GCD is "+str(no2)
    else:
      a=no1%no2
      gcd(no2,a)
  no1=int(raw_input("enter a number"))
  no2=int(raw_input("enter another number"))
  gcd(no1,no2)
except Exception as e:
  print e