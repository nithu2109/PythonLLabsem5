num=int(input("Enter a number : "))
def factors(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
         def isprime():
             count =0
             for j in range(2,i):
                 if(i%j==0):
                     count +=1
             if(count==0):
                 print(i)
        isprime()

factors(num)

          