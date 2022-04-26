#keyword arguments
def bottledetails(name,color,capacity,height):
     print('name:{} color:{} capacity:{} height:{}'.format(name,color,capacity,height))
	 
bottledetails('zirpy','red',1,10)

#keyword arguments
def bottledetails(name,color,capacity,height):
     print('name:{} color:{} capacity:{} height:{}'.format(name,color,capacity,height))
	
bottledetails(color='red',name='zirpy',capacity=1,height=10)
# *args
def printall(*args):
     for arg in args:
	     print(arg)
printall(1,20,50,100,33)

#variable no of arguments
def multiply(*args):
    mult=1
    for number in args:
	     mult=mult*numbers
    return mult
result=multiply(1,2,3,4,5)
print(result)

#what is the o/p of this program
def multiply(start,*args):
    mult=start
    for number in args:
	    mult=mult*numbers
    return mult
result=multiply(10,1,2,3,3,4)
print(result)