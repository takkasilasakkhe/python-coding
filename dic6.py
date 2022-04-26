d1={12:{'class':'b.come fy','percentage':78.50}
    14:{'class':'b.come fy','percentage':77},
    15:{'class':'b.come fy','percentage':88}
}
print(d1)
rollnumber=int(input('enter your roll number'))
percentage=d1[rollnumber]["perecentage"]
if(percentage>40):
    print('passed')
else:
    print('failed')