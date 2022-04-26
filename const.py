#constructor
def __init__(self,color,capacity):
    self.color=color
    self.capacity=capacity
    print('constructor')
def __del__(self):
    print('destructor')
#functions/behaviour
def wash(self):
    print('washing')
def setcap(self):
    print('setcap')
def fillwater(self):
    print('fillwater')
#object creation
bottle1=bottle("green",2)
bottle2=bottle("pink",3)

print(bottle1)
print(bottle1.color)
bottle1.wash()
	