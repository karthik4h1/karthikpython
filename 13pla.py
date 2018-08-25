K=int(input())
sum=0
while(K!=0):
  m=K%10
  sum+=m**2
  K=K//10
print(sum)
