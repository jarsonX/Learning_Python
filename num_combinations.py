#The formula for the number of combinations of length 
#r from a set of n objects.

def numCombinations(n, r):
    return factorial(n) / (factorial(r)*factorial(n-r))

def factorial(num):
    for x in range(1, num):
        num *= x
    if num == 0:
        return 1
    else:
        return num
 
#Examples
print(numCombinations(100, 50))
print(numCombinations(10, 5))
print(numCombinations(4, 4))