k=input()
c=0
for i in k:
  if(i.isdigit() or i.isalpha()or i==' ' or i=='_'):
    continue
  else:
    c=c+1
print(c)

