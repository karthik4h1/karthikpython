e0,b0=map(int,input().split())
e1,b1=map(int,input().split())
c0=(e0*60)+b0
d0=(e1*60)+b1
d1=c0-d0
c1=d1//60
d1%=60
print(c1,d1,sep=" ")
