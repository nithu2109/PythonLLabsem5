n=int(input("Enter the value of n : "))
mylist=[]
for i in range(0,n):
 i=int(input("Enter the element : "))
 mylist.append(i)
mylist.sort()
print("List before inserting : ")
print(mylist)
num=int(input("Enter an Element to Insert : "))
for i in range (len(mylist)):
  if mylist[i]>num:
     mylist.insert(i,num)
     break
if mylist[len(mylist)-1]<num:
        mylist.insert(len(mylist),num)

print(mylist)