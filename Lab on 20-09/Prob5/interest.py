def simp_int(p,n,i=11.5):
    amount=(p*i*n)/100
    return amount
def comp_int(p,n,i=11.5):
    amt=p*((1+(i/100))**n)
    return amt