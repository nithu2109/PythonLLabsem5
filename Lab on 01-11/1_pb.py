class EB_amount():
    def __init__(self):
        self.__bill=0
        self.__units=0
        
    def inputdetail(self):
        self.__units=int(input("Enter Units Used : "))
        
    def calculate(self):
        if(self.__units<=200):
            self.__bill=self.__units*3
        elif(self.__units>200 and self.__units<=500):
            self.__bill=self.__units*4
        elif(self.__units>500):
            self.__bill=self.__units*5.5

    def Printdetail(self):
        print("Bill             :",self.__bill)



eb=EB_amount()
eb.inputdetail()
eb.calculate()
eb.Printdetail()