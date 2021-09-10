import math
x1=float(input("Enter x cordinate of  first point"))
y1=float(input("Enter y cordinate of first point"))
x2=float(input("Enter x cordinate of second point"))
y2=float(input("Enter y cordinate of second point"))
d=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print("Distance Between 2 points is:",math.sqrt(d))