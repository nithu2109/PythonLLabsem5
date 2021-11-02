class Student():
    def __init__(self):
        self.__student_number=0
        self.__name=""
        self.__study_of_degree=""

    def rno(self):
     self.__student_number=int(input('Enter the regno : '))
    def name(self):
     self.__name=input('Enter the name : ') 
    def degree(self):
     self.__study_of_degree=input('Enter the Degree : ')
    def rnos(self):
     return self.__student_number
    def names(self):
     return self.__name
    def degrees(self):
     return self.__study_of_degree
    

class Exam(Student):
    def __init__(self):
        super().__init__()
        self._l=[0,0,0,0,0,0]
    def inputdetails(self):
        super().rno()
        super().name()
        super().degree()
        for i in range(6):
            self._l[i]=int(input('Enter the marks of subject '))

class Result(Exam):
    def __init__(self):
        super().__init__()
        self.total_sum=0
        self._avg=0
    def calculate(self):
        sum=0
        for i in range(6):
            sum+=self._l[i]
        self.total_sum=sum
        self.avg=self.total_sum/6
    def printer(self):
        print("Registration number : ",super().rnos())
        print("Name : ",super().names())
        print("Degree : ",super().degrees()) 
        print("Score in all 6 subjs:",self._l)
        print("Total Score is :",self.total_sum)
        print("Average score is :",self.avg)

r=Result()
r.inputdetails()
r.calculate()
r.printer()





res=Result()
