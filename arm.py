num = int(input("Enter a number: "))
p=len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** p
   temp //= 10
if num == sum:
   print("yes")
else:
   print("no")
