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


#SORTING-ALGORITHMS---------------------------------------------------------------|
#Algorithms that take as input a list and produce as output a sorted version of
#that list. Examples include: bubble sort, insertion sort, merge sort, shell sort,
#quick sort and heap sort.

#Bubble sort, O(n^2)
def sort_with_bubbles(lst):
    swap_occurred = True

    while swap_occurred:

        swap_occurred = False        

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:                
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                swap_occurred = True

    return lst     

print(sort_with_bubbles([4, 3, 5, 2, 1]))

#Insertion sort, O(n^2)
#Moves one item at a time through the list and puts it in the right location
#relative to the items that have been alredy sorted, i.e. compares the item
#with every previous item in the list (which might be a lot of comparisons).

def sort_with_select(a_list):
    
    for i in range(len(a_list)):
        
        minIndex = i

        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[minIndex]:
                minIndex = j

        minValue = a_list[minIndex]
        del a_list[minIndex]
        a_list.insert(i, minValue)
    
    return a_list

print(sort_with_select([5, 3, 1, 2, 4]))

#Merge sort, n log(n)
#Breaks the list into individual items, merge two adjacent lists and compares
#the lowest item in each. Whichever is lower, is added to the new list.


