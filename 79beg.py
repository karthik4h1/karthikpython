import math
n,m=map(int,input().split())
k=n*m
i=int(math.sqrt(k)) 
if(k==i*i):
  print("yes")
else:
     print("no")

