a=int(input())
b=input().split()
k=len(b)
for i in range(0,k):
  q=b.count(b[i])
  if(q<2):
    print(b[i],end="")
