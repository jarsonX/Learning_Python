# Napisz program, który znajduje 10 początkowych liczb ciągu Fibonacciego.
# W ciągu Fibonacciego każda kolejna liczba jest sumą dwóch poprzednich.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range (1, 11):
    print('fib(', i, ') to ', fib(i), sep='')        