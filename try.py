#try ,except statements
class join:
    def __init__(self):
	    print('joined')
	def welcome(self):
	    print('welcome')
	def __del__(self):
	    print('destructor')
	def members(self):
	    try:
		    members=["nandu","raj","ram
		    print(members[3])
        except:
		     print('exception occured')
j1=join()
j1.welcome()
j1.members()