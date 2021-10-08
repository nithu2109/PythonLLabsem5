def getmarks(n):
    for i in range(0,n):
        m='marks'+str(i+1)
        print("Enter marks of rollno:",sd['rno'+str(i+1)])
        marks=int(input())
        if(marks>=0 and marks<=100):
              sd[m]=marks
        else:
            bool=True
            while(bool):
                print("Enter valid marks:")
                marks=int(input())
                if(marks>=0 and marks<=100):
                    bool=False
                    sd[m]=marks
def passedDetails(sd,n):
    ct=0
    for i in range(0,n):
        m=sd.get('marks'+str(i+1))
        if(m>=50):
            ct=ct=ct+1
    pr=(ct/n)*100
    print("Passrate:",pr)
def failedDetails(sd,n):
    ct=0
    for i in range(0,n):
        m=sd.get('marks'+str(i+1))
        if(m<50):
            ct=ct=ct+1
    fr=(ct/n)*100
    print("Failrate:",fr)
def highLowMarks(sd,n):
    low=100
    high=0
    for i in range(0,n):
        m=sd.get('marks'+str(i+1))
        if(m<low):
            low=m
        if(m>high):
            high=m
    print("Highest mark:",high)
    print("Lowest mark:",low)
n=int(input("Enter the value of n:"))
sd={}
for i in range(0,n):
    sno='rno'+str(i+1)
    sname='name'+str(i+1)
    rno=int(input("Enter your rollno:"))
    name=input("Enter your name:")
    sd[sno]=rno
    sd[sname]=name
print(sd)
getmarks(n)
print(sd)
passedDetails(sd,n)
failedDetails(sd,n)
highLowMarks(sd,n)
