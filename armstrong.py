num=153
#num=1534
l=len(str(num))
temp=num
sum=0
while num>0:
  rem=num%10
  sum=sum+rem**l
  num//=10
if temp==sum:
  print("armstrong number")
else:
  print("not armstrong number")
