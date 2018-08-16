k=int(input())
for i in range(1,k+1):
    for j in range(1,k+1):
        if i*j==k and i != 1:
            d=0
            for c in range(2,i):
                if i%c==0:
                    d=d+1
            if d==0:
              print(i,end=" ")
