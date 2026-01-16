day=int(input("enter your number\n1.monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday"))%7
if day==1:
  print("Monday")
elif day==2:
  print("Tuesday")
elif day==3:
  print("Wednesday")
elif day==4:
  print("Thursday")
elif day==5:
  print("Friday")
elif day==6:
  print("Saturday")
elif day==0:
  print("Sunday")
else:
  print("Invalid Choice")