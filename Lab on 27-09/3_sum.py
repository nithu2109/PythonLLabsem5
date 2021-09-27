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
 
matrix = [[ 6, 5, 4 ],
       [ 1, 2, 5 ],
       [ 7, 9, 7 ]]

Sum(matrix)