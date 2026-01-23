def fibonacci_series(n):
  n=9
  a,b=0,1
  print("Fibonacci series:")
  for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

fibonacci_series(9)
