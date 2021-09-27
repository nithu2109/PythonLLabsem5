def rem_dup(list):
    print("Original List : ",list)
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print("The list Without Duplicates : ",new_list)
    


list=[]
n=int(input("Enter number of elements : "))
for i in range(0,n):
    element=int(input())
    list.append(element)

rem_dup(list)