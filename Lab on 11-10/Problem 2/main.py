import palindrome as pd
lol=[]
n=int(input("Enter the number of words:"))
for i in range(0,n):
    l=[]
    s=input("Enter the word:")
    l.append(s)
    lol.append(l)
for i in lol:
    for j in i:
        if(pd.recpalindrome(j)==True):
            print(j,"is a palindrome")
        else:
            print(j,"is not a palindrome")
