x=('key1','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
x=("key1","key2","key3")
y="hello"
thisdict=dict.fromkeys(x,y)
print(thisdict)
x=('key1','key2','key3')
thisdict=dict.fromkeys(x)
print(thisdict)
thisdict={"brand":"ford","model":"Nano","year":1964}
x=thisdict.setdefault("color","white")
print(x)
x=thisdict.setdefault("model","hello")
print(x)
thisdict["brand"]="hai"
print(thisdict)