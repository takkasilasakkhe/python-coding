rank=int(input('enter your rank'))
if rank<=1000:
    print('you got college1')
elif rank>1000 and rank<=10000:
    print('you got college2')
elif rank>10000 and rank<=40000:
    print('you got college3')
else:
    print('sorry no college available for your rank')	