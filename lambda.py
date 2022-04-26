#normal function
def cube(num):
    return num*num*num
print(cube(2))

#lambda function
result=(lambda num:num*num*num)(3)
print(result)
      
	  
cube=lambda num:num*num*num
print(cube(3))

#filter
def iseven(num):
    return num%2==0
numbers=[10,11,23,22,80,87]
result=filter(iseven,numbers)
print(list(result))
#lets use lambda function instead of iseven
numbers=[10,11,23,22,80,87]
result=filter(lambda num:num%2==0,numbers)
print(list(numbers))