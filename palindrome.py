num=121
temp=num
rev=0
while num!=0:
  rem=num%10
  rev=rev*10+rem
  num=num//10
print("Rev",rev)
if temp==rev:
  print(f"{rev} is palindrome number")
else:
  print(f"{rev} is not a palindrome number")