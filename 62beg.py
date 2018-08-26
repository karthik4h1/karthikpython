n=input()
a=n.count('1')
b=n.count('0')
K=len(n)
if(K==a+b):
  print("yes")
else:
    print("no")
