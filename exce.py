#syntax error
class join:
   def __init__(self):
	     print('constructor')
   def welcome(self):
	      print('welcome')
j1=join()
j1.welcome()

#logical error
class join:
   def __init__(self):
        print('joined channel')
   def welcome(self):
	    print('welcome to the channel')
   def __del__(self):
	    print('destructor')
		
   def members(self):
        members=['nandu','raju','ramu']
        print(members[2])
j1=join()
j1.welcome()
j1.members()