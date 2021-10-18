import stack as s

def rec_stack(s1,s2):
    if s.isempty(s1):
        print("The revrsed value from another stack")
        print(s2)
    else:
        y,s1=s.pop(s1)
        s2=s.push(s2,y)
        return rec_stack(s1,s2)

n=int(input("Enter the value of n:"))
s1=()
for i in range(n):
    x=int(input("Enter the element:"))
    s1=s1+(x,)
s2=()
rec_stack(s1,s2)
