'''
Name:Narendra Raj Rk
Set:1
Question:4c
'''


timestarted = 6 * 3600 + 52 *60
easypace = 2 * (8 * 60 + 15 )
tempopace = 3 * (7 * 60 + 12 )
totaltime =timestarted+easypace+tempopace
hours = totaltime/3600
#print(hours)
remainingsec= totaltime%3600
#print(remainingsec)
minutes = remainingsec/60
#print(minutes)
seconds = remainingsec% 60
print "reached home for breakfast at:",hours,":",minutes,":",seconds,"AM"
