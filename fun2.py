# returning from function
# used to return data and exit from the function
# program to return data from function
def cubeofnumber(number):
        cube=number*number*number
        return cube
	
	
result=cubeofnumber(10)
print('result is',result)





# what if nothing is returned from the return statement result is none
def cubeofnumber(number):
        cube=number*number*number
        return 
	
	
	
print(cubeofnumber(20))
#pass by reference,pass by value
#memory location
a=10
list=[10,20,30]
print(a)
print(list)
list=a
print(list)
