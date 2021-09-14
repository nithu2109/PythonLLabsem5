maths=float(input("Enter marks in first subject: "))
physics=float(input("Enter marks in second subject: "))
chemistry=float(input("Enter marks in third subject: "))
biology=float(input("Enter marks in fourth subject: "))
computers=float(input("Enter marks in fivth subject: "))
total=maths+physics+chemistry+biology+computers
percent=total/5
if(percent>=90):
    print("Grade A")
elif(percent>=80):
    print("Grade B")
elif(percent>=70):
    print("Grade C")
elif(percent>=60):
    print("Grade D")
elif(percent>=40):
    print("Grade B")
elif(percent<40):
    print("Grade B")