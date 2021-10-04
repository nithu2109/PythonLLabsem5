def Sum(matrix):
 
    i,j = 0,0
    r,c=3,3
    upper_sum = 0
    lower_sum = 0
     
    # to calculate sum of upper triangle
    for i in range(r):
        for j in range(c):
            if (i <= j):
                upper_sum += matrix[i][j]
    print("Upper sum is ", upper_sum)
    # to calculate sum of lower
    for i in range(r):
        for j in range(c):
            if (j <= i):
                lower_sum += matrix[i][j]
    print("Lower sum is ", lower_sum)
 
       
n=int(input("Enter the value of n"))
l=[]
for i in range(0,n):
 il=[]
 for j in range(0,n):
  a=int(input("Enter the element:"))
  il.append(a)
 l.append(il)
 
print("The matrix in list of list format",l)

Sum(l)