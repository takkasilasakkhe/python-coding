# using except multiple times
class join:
    def __init__(self):
	    print('joined')
    def welcome(self):
	    print('welcome')
    def __del__(self):
	    print('destructor')
    def members(self):
	    try:
		    members=["nandu","raj","ram"]
		    print(members[3])
        except indexerror:
		    errorinfo=sys.exc__info()
			print(errorinfo[0],errorinfo[1])
		except i0error:
		    print('execute')
		except importerror:
		    print('import error')
		except:
		    print('final except')
			
j1=join()
j1.welcome()
j1.members()