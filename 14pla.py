k=input()
a=input()
vowels=('a','e','i','o','u')
for x in a.lower():
    if x in vowels:
        a=a.replace(x,'')
print(a[::-1])
