#union operation
print("union operation")
a={10,20,30,40}
b={20,80,70,100}
abunion=a.union(b)
print(abunion)

#intersection
print("intersction")
a={10,20,30,40}
b={20,80,70,30,100}
abintersection=a.intersection(b)
print(abintersection)

#difference
print("difference")
a={10,20,30,40}
b={20,80,70,100}
abdifference=a.difference(b)
print(abdifference)
abdifference=b.difference(a)
print(abdifference)

'''#symmetric difference
print("symmetric difference")
a={10,20,30,40}
b={20,80,70,100}
absymmetricdiff=a.symmetricdiff(b)
print(absymmetricdiffs)'''