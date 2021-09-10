def maximum(a,b,c):
    if(a>=b & a>=c):
        return a
    elif (b>=a & b>=c):
        return b
    else:
        return c

a=198
b=67
c=9
print(max(a,b,c))