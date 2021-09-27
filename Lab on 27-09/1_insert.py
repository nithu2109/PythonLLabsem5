num=int(input("Enter an Element to Insert : "))
list=[1,2,3,7,9,10]
for i in range (len(list)):
  if list[i]>num:
     list.insert(i,num)
     break
if list[len(list)-1]<num:
        print("yep")
        list.insert(len(list),num)

print(list)