class plasticbottle(bottle):
    def __init__(self):
	    print('childconstructor')
    def fillsoda():
	    print('filling soda')

plasticbottle=plasticbottle()

#using super function
class copperbottle(bottle):
   def __init__(self,color,capacity):
      super().__init__(color,capacity)
   def morningwater():
      print('morningwater')
print(copperbottle.companyname)
copper1=copperbottle("orange",7)
copper1.washk()