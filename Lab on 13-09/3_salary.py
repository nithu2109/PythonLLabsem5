basicpay=int(input("Enter salary of a person  "))
gross_sal=0
if(basicpay<= 10000):
    HRA=(20*basicpay)/100
    DA=(80*basicpay)/100
    gross_sal=HRA+basicpay+DA
    
elif(basicpay<=20000):
    HRA=(25*basicpay)/100
    DA=(90*basicpay)/100
    gross_sal=HRA+basicpay+DA  
else:
    HRA=(30*basicpay)/100
    DA=(95*basicpay)/100
    gross_sal=HRA+basicpay+DA
print("Gross Salary :",gross_sal)