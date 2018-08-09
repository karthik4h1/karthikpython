x=(input())
if((x>='a' and x<='z') or (x>='A' and x<='Z')):
	if(x in ['a','e','i','o','u','A','E','I','O','U']):
		print('vowel')
	else:
		print('consonant')
else:
    print('invalid')
