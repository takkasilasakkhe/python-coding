#map
def capitableletter(name):
    return name.upper()
friends=['jenny','marry','loggy']
result=map(capitableletter,friends)
print(list(result))


#use lambda function
friends=['jenny','marry','loggy']
result=map(lambda name:name.upper(),friends)
print(list(result))

#reduce
def addall(a,b):
    return a+b
numbers=[20,1,3,10,5]
result=reduce(addall,numbers)
print(result)


def addall(a,b):
    return a+b
numbers=[20,1,3,10,5]
result=reduce(addall,numbers,5)
print(result)

#usig lambda function
numbers=[20,1,3,10,5]
result=reduce(lambda a,b:a+b,numbers,10)
print(results)

