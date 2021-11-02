class Distance():
    def __init__(self):
        self.distance={}
    def getinput(self):
        for i in range(1,6):
            self.distance[i]={"feet":int(input("Enter feets : ")),"inches":int(input('Enter the inches: '))}

class Operation(Distance):
    def __init__(self):
        super().__init__()
        self.result=[0,0]

    def Average(self):
        print("Calculating...")
        sum_feet=0
        sum_inch=0
        avg_ft=0
        avg_inch=0
        for a,b in self.distance.items():
            sum_feet+=b["feet"]
            sum_inch+=b["inches"]
        sum_inch+=(sum_feet*12)
        sum_inch/=5
        avg_ft=sum_inch//12
        avg_inch=sum_inch%12
        self.result[0]=avg_ft
        self.result[1]=avg_inch
        print(self.result[0],self.result[1])

    def Add_distance(self):
        print('Adding 1st and 2nd distance....')
        totfeet=self.distance[1]['feet']+self.distance[2]['feet']
        totinches=self.distance[1]['inches']+self.distance[2]['inches']
        while(totinches>=12):
            totfeet+=1
            totinches-=12
        self.result[0]=totfeet
        self.result[1]=totinches
        print(self.result[0],self.result[1])

    def Maximum(self):
        # print("Maximum Value is ..")
        max=0
        max_val=0
        count=1
        for x,y in self.distance.items():
            cur_val=y["feet"]*12+y["inches"]
            if(cur_val>max_val):
                max=count
                max_val=cur_val
                count=count+1
        self.result[0]=self.distance[max]['feet']
        self.result[1]=self.distance[max]["inches"]
        print("Maximum Feet : ",self.result[0]," Maximum inches : ",self.result[1])


    def Display(self):
        print("Nested dictionary value is : ",self.distance)
     




o=Operation()
o.getinput()
o.Average()
o.Add_distance()
o.Maximum()
o.Display()



