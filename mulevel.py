#multilevel inheritance
class class1:
   def subscribe(self):
       print('subscribe')
class class2(class1):
   def join(self):
       print('joined')
class class3(class2):
   def details(self):
      print('class3 details')
cl3=class3()
cl3.details()
cl3.join()
cl3.subscribe()