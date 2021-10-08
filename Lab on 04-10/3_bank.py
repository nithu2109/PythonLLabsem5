def Debit(cd,acn,db_amt):
    for i in range(n):
        if(cd['anum'+str(i+1)]==acn):
            if(cd['balance'+str(i+1)]>=db_amt):
                cd['balance'+str(i+1)]-=db_amt
                print("Amount debited successfully")
    print(cd)

def Credit(cd,acn,cd_amt):
    for i in range(n):
        if(cd['anum'+str(i+1)]==acn):
            cd['balance'+str(i+1)]+=cd_amt
    print(cd)
n=int(input("Enter the number of customers : "))
cd={}
for i in range(n):
    an='anum'+str(i+1)
    bal='balance'+str(i+1)
    accno=int(input("Enter the account number : "))
    balance=int(input("Enter the balance amount : "))
    cd[an]=accno
    cd[bal]=balance
print(cd)
acn=int(input("Enter  account number from which you want to withdraw amount : "))
db_amt=int(input("Enter the amount to be withdrawn : "))
Debit(cd,acn,db_amt)
acc=int(input("Enter account number to which you want to deposit money : "))
cd_amt=int(input("Enter the amount to be deposited : "))
Credit(cd,acn,cd_amt)
