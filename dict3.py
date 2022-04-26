thisdict={"brand":"ford","model":"Nano","year":1964}
thisdict.update({"year":2021})
print(thisdict)
thisdict.update({"name":"hari"})
print(thisdict)
print(thisdict.items())
thisdict["brand"]="nmmm"
print(thisdict)
thisdict.pop("brand")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["model"]
print(thisdict)