name =input('enter your name')
print('your name is:',name)
doorno,street,city,state =input('enter your address-seperated by comma').split(",")
print('address is:street{},state{}',format(street,state))