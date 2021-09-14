import math
a=int(input("Enter 'a' value of quadratic equation"))
b=int(input("Enter 'b' value of quadratic equation"))
c=int(input("Enter 'c' value of quadratic equation"))
d=(b*b)-(4*a*c)
if(d>0):
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("the roots of the equation are",root1," ",root2)
elif(d==0):
    root1 = root2 = -b / (2 * a)
    print("the roots of the equation are",root1," ",root2)
elif(d<0):
   root1 = root2 = -b / (2 * a)
   imaginary = math.sqrt(-d) / (2 * a)
   print("the roots of the equation are",root1," ",root2)