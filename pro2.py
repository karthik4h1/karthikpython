def reduceN(j,k):
    if k<=0: return j
    if j==0: return 10
    p1=reduceN(j//10,k)*10+j%10
    p2=reduceN(j//10,k-1)
    if p1<p2:
        return p1
    else:
        return p2
j,k=input().split()
j,k=int(j),int(k)
print(reduceN(j,k))
