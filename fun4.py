#keyword arguments
def bottledetails(**kwargs):
    for key,value in kwargs.items():
	    print('{}:{}'.format(key,value))
bottledetails(color='red',name='zirpy',capacity=1,height=10)

#passing *args,**kwargs from caller
def eatme(apple,banana,orange,grapes):
     print(apple,banana,orange,grapes)
fruits=(10,5,1,9,)
eatme(*fruits)

#yield generators
def coconutcapacity(number):
    calories=number*19
    return calories
    print('super')
calories=coconutcapacity(2)
print(calories)
#yield
def coconutcapacity(number):
    calories=number*19
 
    yield calories
    print('super')
calories=coconutcapacity(2)
print(calories)
for i in calories:
     print(i)
