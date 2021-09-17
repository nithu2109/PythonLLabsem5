list1=[]
n=int(input("enter the number of elements "))
for i in range (0,n):
   element=int(input())
   list1.append (element)

poscount=0
possum=0
negsum=0
zerocount = 0
negcount = 0
for i in range (0, n): 
    if (list1[i]>0):
        poscount+=1
        possum+=list1[i] 
    elif (list1[i]==0):
        zerocount+=1
    else:
        negcount+=1
        negsum+=list1[i]
avgpos= (possum/poscount)
avgneg= (negsum/negcount) 
print("Number of Positive Numbers:",poscount)
print("Sum of Positive Numbers:",possum)
print("Average of Positive Numbers:",avgpos)
print("\n")
print("Number of Negative Numbers:",negcount)
print("Sum of Negative Numbers:",negsum)
print("Average of Negative Numbers:",avgneg)
print("\nthe no.of zeroes are", zerocount)
