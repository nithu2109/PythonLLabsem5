def push(L,x):
    L=L+(x,)
    return L

def pop(L):
    M=L[:len(L)-1]
    return L[len(L)-1],M

def isempty(L):
    if not L:
        return True
