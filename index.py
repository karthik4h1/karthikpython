num1=int(input())
num2=[int(a) for a in input().split()]
for b in range(num1):
  print(num2[b],b,sep='',end="\n")

