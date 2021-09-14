side1=int(input("Enter first side: "))
side2=int(input("Enter second side: "))
side3=int(input("Enter third side: "))

if (side1==side2) & (side2==side3):
   print("The triangle is equilateral triangle")
elif (side1==side2) | (side2==side3) | (side3==side1) :
   print("The triangle is isoceles triangle")   
else:
   print("The triangle is scalene triangle")