import math
def standard_dev(*n):
 sum=0
 for i in n:
  sum+=i
  mean=sum/len(n)
 for i in n:
  t=0
  t+=(i-mean)**2
  p=math.sqrt(t/len(n))
  return p

print("The standard deviation:", standard_dev(2,3,4,5))
