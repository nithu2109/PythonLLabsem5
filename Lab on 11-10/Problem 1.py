import math
def recseries(x,n):
    if(n==1):
        return 1
    else:
        num=(2**(n-1))**x
        d=2**(n-1)
        return ((num/d)+recseries(x,n-1))
n=int(input("Enter the value of n:"))
x=int(input("Enter the value of x:"))
val=recseries(x,n)
print("The sum of series is",val)
