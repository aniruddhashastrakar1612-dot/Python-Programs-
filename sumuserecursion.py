#sum of digit using recursion
def sum_of_digit(num):
  if num==0:
    return 0
  else:
    return num%10+sum_of_digit(num//10)
sum_of_digit(int(input("enter the number")))