n1=int(input("enter the value of n1"))
n2=int(input("enter the value of n2"))
ch=input("enter the choice\n+.add\n-.sub\n*.mul\n/.div")
match(ch):
  case "+":  #ch=="+"
    print(f"addition of {n1} and {n2}:{n1+n2}")
  case "-":
    print(f"subtraction of {n1} and {n2}:{n1-n2}")
  case "*":
    print(f"multiplication of {n1} and {n2}:{n1*n2}")
  case "/":
    print(f"division of {n1} and {n2}:{n1/n2}")
  case _:
    print("invalid choice")
