class Employee():
    def __init__(self):
        self._emp_id=0
        self._name=""
        self._designation=""
        self._salary=0
    def getdetails(self):
        self._emp_id=int(input("Enter Employee ID : "))
        self._name=input("Enter Name : ")
        self._designation=input("Enter Designation : ")
        
class Permanent(Employee):
    def __init__(self):
        super().__init__()
        self.basic=0
        self.DA=0
        self.TA=0
        self.HRA=0
    def getdetails(self):
        super().getdetails()
        self.basic=int(input('Enter the Basic Salary:'))
        self.DA=int(input('Enter  DA :'))
        self.TA=int(input('Enter  TA :'))
        self.HRA=int(input('Enter  HRA :')) 
    def sal_calc(self):
      self._salary=self.basic+self.DA+self.TA+self.HRA
    def printer(self):
        print("Employee ID           : ",self._emp_id)
        print("Employee Name         : ",self._name)
        print("Employee Designation  : ",self._designation)
        print("Salary                : ",self._salary)

class Contract(Employee):
    def __init__(self):
        super().__init__()
        self.num_hrs=0
        self.wages_per_hr=0
    def getdetails(self):
      super().getdetails()
      self.num_hrs=int(input('Enter the no of hrs :'))
      self.wages_per_hr=int(input('Enter the wage per hr :'))
    def sal_calc(self):
     self._salary=self.num_hrs*self.wages_per_hr
    def printer(self):
        print("Name :",self._name)
        print("Emp id :",self._emp_id)
        print("Designation :",self._designation)
        print("Salary :",self._salary)

print("Permanent Employee")
p=Permanent()
p.getdetails()
p.sal_calc()


print('-------------Permanent Employee Details--------------')
p.printer()

print("\n")
print('------------------------------------------------------')
print('Contract Employee')
print("\n")
c=Contract()
c.getdetails()
c.sal_calc()
print('-------------Contract Employee Details--------------')
c.printer()
print('----------------------------------------------------')



