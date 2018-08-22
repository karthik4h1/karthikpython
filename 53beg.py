K=int(input())
tot=0
while(K>0):
    dig=K%10
    tot=tot+dig
    K=K//10
print(tot)
