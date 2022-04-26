thisdict={"brand":"ford","model":"Nano","year":1964}
x=thisdict.keys()
print(x)
thisdict["color"]="red"
print(x)
print(thisdict)
x=thisdict.values()
print(x)
print(thisdict["brand"])
thisdict["year"]=2020
print(thisdict)
print(thisdict.items())
if "model" in thisdict:
   print("yes,moedl is one of the key in thisdict")