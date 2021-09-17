import math
n=int(input("Enter the number of terms :"))
x=int(input("Enter the value of x in degrees :"))

sum=0
sign=0
for i in range(n):
 sign=(-1)**i
pi=22/7
y=x*(pi/180)
sum += ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
print("Sum of Sine series:",sum)
sum=1
sign=-1

for i in range(2,n,2):
 pi=22/7
y=x*(pi/180)
sum+=((y**i)/math.factorial(i))*sign
sign=-sign
print("Sum of Cosine series: ",sum)
sum=1

for i in range(1,n):
 pi=22/7
y=x*(pi/180)
sum+=((y**i)/math.factorial(i))
print("Sum of Exponential series: ",sum)