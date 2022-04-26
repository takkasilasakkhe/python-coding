'''marks =[50,20,90,65,98,90]
print(marks)
print(marks*2)
print(len(marks))
print(type(marks))
marks[1]=100
print(marks)
marks[2]=11
print(marks)
friends=["hari","raju","ramu","ravi","ran"]
friends[1]="venu"
print(friends)
print(type(friends))
print(marks+friends)
print(friends*2)
friends.append("india")
print(friends)
friends.append("tokyo")
print(friends)
friends.extend(["hello","hai"])
print(friends)'''
#adding an items to the list
names=["honey","sona","shannu","sham","sasi"]
del names[0]
print(names)
names.insert(1,"sony")
print(names)
names.insert(2,"harsha")
print(names)
names[1:1]=["a","b","c"]
print(names)
names[1:4]=[1,2,3,4]
print(names)
del names[1]
print(names)
del names[2:5]
print(names)