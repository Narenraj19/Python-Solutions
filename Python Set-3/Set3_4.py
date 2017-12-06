'''
Name : Narendra Raj RK
Setno: 3
Question_no:4 
Description:Modify the above program to print only the words that have no “e” 
             and compute the percentage of the words in the list have no “e.”
'''



def has_no_e(strlist):
     e=[]
     we=[]
     for i in strlist:
         if 'e' in i:
             e.append(i)
         elif 'E' in i:
             e.append(i)
         else:
             we.append(i)
     original_len=float(len(strlist))
     len_without_e=len(we)
     percentage=(len_without_e/original_len)*100
     print percentage
 str=raw_input("str")
 strlist=str.split(' ')
 has_no_e(strlist)



