#find vowels and consonant in your name
name=input('enter your name')
vowelslist=['a','e','i','o','u']
for i in name:
    if i in vowelslist:
	    print(i,'it is vowel')
    else:
	    print(i,'it is consonant')
		
#find if your name has a vowel in your name
name=input('enter your name')
vowelslist=['a','e','i','o','u']
for i in name:
    if i in vowelslist:
	    print(i,'found vowel')
	    