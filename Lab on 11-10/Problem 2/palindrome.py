def recpalindrome(s):
    n=len(s)
    if(len(s)<=1):
        return True
    elif(s[0]==s[n-1]):
        return recpalindrome(s[1:-1])
    else:
        return False
