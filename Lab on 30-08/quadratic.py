import math

a=1
b=32
c=6
d=(b*b)-(4*a*c)
if(d>0):
    res1=((-1*b)+math.sqrt(d))/2*a
    res2=((-1*b)-math.sqrt(d))/2*a
    print("Roots are real and distinct ",res1,res2)
elif(d==0):
    res1=((-1*b)+math.sqrt(d))/2*a
    print("Roots are real and equal ",res1)
else:
    print("Roots are imaginary")
