j,k=map(int,input().split())
def gcd(j,k):
  if j==0 or k==0:
    return 0
  if j==k:
    return j
  if j>k:
    return gcd(j-k,j)
  return gcd(j,k-j)
gcd(j,k)
print(gcd(j,k))
