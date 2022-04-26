#heirachical inheritance
class class1:
   def subscribe(self):
       print('subscribe')
class class2(class1):
   def join(self):
       print('joined')
class class3(class1):
   def details(self):
      print('class3 details')
class class4(class1):
   def details(self):
      print('class4 details')