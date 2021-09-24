import math
def compute(r=1,h=2):
    volume=math.pi*(r*r)*h
    return volume
print("Volume : ",compute())
print("Volume : ",compute(1,2))