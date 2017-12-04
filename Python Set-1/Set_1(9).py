'''
Name : Narendra Raj RK
Setno: 1
Question_no:9
Description:To Find the value and type of  width,height and delimiter
'''

try:
  def fn(width,height,delimiter):
    w=width/2
    w1=width/2.0
    h=height/3
    a=1+2*5
    d=delimiter*5
    print(w,type(w))
    print(w1,type(w1))
    print(h,type(h))
    print(a,type(a))
    print(d,type(d))
  width=int(raw_input("enter the width"))
  height=int(raw_input("enter the height"))
  delimiter=raw_input("enter the delimiter")
  fn(width,height,delimiter)
except Exception as e:
  print e