'''
Name:Narendra Raj RK
Set:1
Ques.No:8
Description:def getRatios(vect1, vect2):
	    """Assumes: vect1 and vect2 are lists of equal length of numbers
	    Returns: a list containing the meaningful values of
	    vect1[i]/vect2[i]"""
'''


def getRatios(vect1, vect2):
    ratios=[]
    for i in range(len(vect1)):
        vect1e=float(vect1[i])
        vect2e=float(vect2[i])
        ratios.append(vect1e/vect2e)
    return ratios
vect1=[18,6,24,100]
vect2=[9,6,8,10]

a=getRatios(vect1,vect2)
print a