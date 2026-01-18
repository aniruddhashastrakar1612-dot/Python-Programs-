n1=int(input("enter the value of n1"))
n2=int(input("enter the value of n2"))
ch=int(input("enter the choice\n1.add\n2.sub\n3.mul\n4.div"))
match(ch):
  case 1:
    print(f"addition of {n1} and {n2}:{n1+n2}")
  case 2:
    print(f"subtraction of {n1} and {n2}:{n1-n2}")
  case 3:
    print(f"multiplication of {n1} and {n2}:{n1*n2}")
  case 4:
    print(f"division of {n1} and {n2}:{n1/n2}")
  case _:
    print("invalid choice")
