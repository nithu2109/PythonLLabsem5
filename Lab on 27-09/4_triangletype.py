n=int(input("Enter the value of n"))
l=[]
for i in range(0,n):
 il=[]
 for j in range(0,n):
  a=int(input("Enter the element:"))
  il.append(a)
 l.append(il)
 
print("The matrix in list of list format",l)
def symmetric(l):
 ct=0
 n=len(l)
 for i in range(0,n):
  for j in range(0,n):
   if(l[i][j]==l[j][i]):
    ct=ct+1
 if(ct==n*n):
  print("The matrix is symmetric")
 else:
  print("The matrix is not symmetric")

def skew(l):
 ct=0
 n=len(l)
 for i in range(0,n):
  for j in range(0,n):
   if(i!=j):
    if(l[i][j]==-l[j][i]):
     ct=ct+1
 if(ct==(n*n)-n):
  print("The matrix is skew")
 else:
  print("The matrix is not skew")

def diagonal(l):
 ct=0
 n=len(l)
 for i in range(0,n):
   for j in range(0,n):
    if((i==j)&(l[i][j]!=0)):
     ct=ct+1
    if((i!=j)&(l[i][j]==0)):
     ct=ct+1
 if(ct==n*n):
  print("The matrix is diagonal")
 else:
   print("The matrix is not diagonal")

def identity(l):
 ct=0
 n=len(l)
 for i in range(0,n):
   for j in range(0,n):
    if((i==j)&(l[i][j]==1)):
     ct=ct+1
    if((i!=j)&(l[i][j]==0)):
     ct=ct+1
 if(ct==n*n):
  print("The matrix is identity")
 else:
  print("The matrix is not identity")

symmetric(l)
skew(l)
diagonal(l)
identity(l)
