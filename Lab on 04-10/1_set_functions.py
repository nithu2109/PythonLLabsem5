mylist=[]
n=int(input("Enter number of decimal values:"))
for i in range(0,n):
    element = int(input())
    mylist.append(element)

mylist=sorted(mylist)
set1=set(mylist)

mylist2=[]
n=int(input("Enter number of decimal values:"))
for i in range(0,n):
    element = int(input())
    mylist2.append(element)

mylist2=sorted(mylist2)
set2=set(mylist2)

def extract():
    set3=set1.difference(set2)
    print("Values Present in set1 and not in set2 : ",set3)
def Unique():
    set3={}
    set3=set1.issubset(set2)
    print(set3)
def Common():
    set3=set1.intersection(set2)
    print("Common Elements from both sets : ",set3)

def Combine():
    set3=set1.union(set2)
    print("Combined Elements from Both sets : ",set3)


extract()
Unique()
Common()
Combine()