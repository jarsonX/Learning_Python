#BASIC ALGORITHMS

#RECURSION------------------------------------------------------------------------|
#A programming method characterized by functions that, during their operation
#call additional copies of themselves. Recursion involves breaking down a problem
#into smaller instances recursively until each of them can be independently
#solved. Solutions to these smaller instances combine to form the solution for
#the original problem.

#recursion example
def factorial(n):
     if n == 1:
          return 1
     else:
          return n * factorial(n-1)

#recursion example
def fibonacci(n):
     if n == 1 or n == 2:
          return 1
     else:
          return fibonacci(n - 1) + fibonacci(n - 2)

#Head recursion occurs when the recursive call is near the beginning of the function,
#before other reasoning or code. Tail recursion occurs when the recursive call is
#closer to the end of the function, after some reasoning or code.
     
#tail recursion example
def count_down_1(start):
     if start <= 0:
         print(start)
     else:
         print(start)
         count_down_1(start - 1)

count_down_1(5)

#head recursion example
def count_down_2(start):
     if start <= 0:
         print(start)
     else:
         count_down_2(start - 1)
         print(start)
         
count_down_2(5)
