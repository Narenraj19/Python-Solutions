
'''
Name : Narendra Raj RK
Setno: 1
Question_no:2
Description:Print string with enough leading spaces so that the last letter of the string is in column 70 of the display.
'''


try:

  def right_justify(s):

    a=s.rjust(70)

    print(a)

  s=raw_input("enter a string:")

  right_justify(s)

except Exception as e:

  print e
