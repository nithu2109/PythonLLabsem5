a=int(input("Enter any number : "))
print("The Factors of ",a ,"are :")
for i in range(1, a + 1):
       if a % i == 0:
           print(i)
print("The Prime Factors of ",a ,"are :")
if(a%2==0):
    print("2")
for i in range (3,(a//2)):
    if(a%i)==0:
        for j in range (2,i):
            if(i%j==0):
                break;
            else:
               print(i)