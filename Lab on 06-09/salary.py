basicpay=int(input("Enter the Basic Pay of An Employee"))
HRA=(10*basicpay)/100
TA=(5*basicpay)/100
pf_percent=float(input("Enter Percentage of Provident fund"))
pf=(pf_percent*basicpay)/100
gross_sal=HRA+basicpay+TA
net_sal=gross_sal-pf
print("Gross Salary",gross_sal)
print("Net Salary",net_sal)