
lastball=4
if(lastball==9):
   print('won the match')
else:
   print('lost the match')
   
#if else
#write a program to check wheter number is even or odd
print('if else statement')
number=int(input('enter a number'))
if(number%2==0):
     print('it is even number')
else:
     print('it is odd number')
#nested if else
print("nested if else")
number=int(input('enter a number'))
if(number%2==0):
    if(number%4==0):
	    print('congrts diveded by both 2 and 4')
    else:
	    print('sorry')