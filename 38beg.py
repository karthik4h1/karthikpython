j,k = input().split()
j,k=int(j),int(k)
j = j ^ k;
k = j ^ k;
j = j ^ k;
print(j,k)
