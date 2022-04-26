#iterating overlist
x=['suresh','john','marry']
print(type(x))

for i in x:
    print(i)
	
	
#iterating over a tuple
x=('suresh','john','marry')
print(type(x))

for i in x:
    print(i)
	
#ierate over a dictionary
numbers={1:'one',2:'two',3:'three'}
print(type(numbers))
for i in numbers:
     print(i)
     print(numbers[i])
	 
#write a program to print you last 2 characters from your name repeat it from 1 to 10
print("last two characters from your name")
name=input('enter your name')
lasttwocharacters=name[-2:]
for number in range(1,11):
    print(lasttwocharacters*number)