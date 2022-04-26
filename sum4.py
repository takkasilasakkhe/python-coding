sum = 10
def calculate():
   global sum
   sum = sum + 20
   currentsum = 200
   totalsum = sum + currentsum
   print(totalsum)
calculate();
print(sum)