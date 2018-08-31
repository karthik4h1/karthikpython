k=int(input())
b=''
while(k!=0):
	t=k%10
	if t%2!=0:
            b=b+' '+str(t)
	k=k//10
print(b[::-1])
