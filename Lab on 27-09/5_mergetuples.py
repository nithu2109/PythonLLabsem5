t1=(2,5,6,7,8,10,12,13)
t2=(1,4,15)
t3=[]
i,j=0,0
while i<len(t1) and j<len(t2):
    if t1[i]<t2[j]:
        t3.append(t1[i])
        i+=1
    else:
        t3.append(t2[j])
        j+=1
#if no element in tuple1
if i==len(t1):
    while j<len(t2):
        t3.append(t2[j])
        j+=1
#if no element in tuple2     
elif j==len(t2):
    while i<len(t1):
        t3.append(t1[i])
        i+=1
t3=tuple(t3)
print(t3)

