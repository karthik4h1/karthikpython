k=int(input())
rev=0
while(k>0):
    dig=k%10
    rev=rev*10+dig
    k=k//10
print(rev)
