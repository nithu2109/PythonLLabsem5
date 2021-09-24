vectype=str(input("Enter Vehicle Type :\n"))
time=int(input("Enter Hours : "))

def pkcharges(vtype, hours):
    total_amt=0
    if(vtype=="c"):
      total_amt= hours*10
    elif(vtype=="b"):
        total_amt= hours*20
    elif(vtype=="t"):
        total_amt= hours*5
    else:
        print("Invalid vehicle type")
        total_amt=0
    return total_amt 

print("Total Parking Charges : ",pkcharges(vectype,time))