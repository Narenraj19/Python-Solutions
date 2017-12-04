'''
Name : Narendra Raj RK
Setno: 2
Question_no:4
Description:Convert binary  to decimal
'''
try:
  def dec_fn(a):
    dec=0
    for i in a:
      dec = dec*2 + int(i)
    print "decimal value:"+str(dec)
  a=raw_input("enter the binary value: ")
  dec_fn(a)
except Exception as e:
  print e