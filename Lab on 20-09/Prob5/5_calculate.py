import interest as I
p=float(input("enter the principle amount : "))
i=float(input("enter the interest rate : "))
n=float(input("enter the time period : "))
total=I.simp_int(p,n)
print("simple interest with default interest arate is:",total)
total=I.simp_int(p,n,i)
print("simple interest with POSITIONAL interest arate is:",total)
total=I.comp_int(p,n)
print("compound interest with default interest arate is:",total)
total=I.comp_int(p,n,i)
print("compound interest with POSITIONAL interest arate is:",total)