import recmergesort as ms
l=[]
n=int(input("Enter the no. of elements:"))
for i in range(0,n):
    l.append(int(input("Enter the element:")))
print("The list before sorting",l)
ms.mergeSort(l)
print("The list after sorting")
print(l)
