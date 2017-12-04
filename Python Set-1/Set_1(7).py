'''
Name : Narendra Raj RK
Setno: 1
Question_no:7
Description: To Find whether the two accepted strings are equal strings
'''


try:
  def isIn(str,str1):
    if(str==str1 or str1==str):
      print "true"
    else:
      print "false"
  str=raw_input("enter a string")
  str1=raw_input("enter second string")
  isIn(str,str1)
except Exception as e:
  print e
