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

def mergesort(lst):
    
    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only
    #one item, we should just return that one-item list.
    
    if len(lst) <= 1:
        return lst
    
    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:

        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(lst) // 2

        #lst[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])

        #And same for the right side.
        right = mergesort(lst[midpoint:])

        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.

        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            #If the first number in left is lower, add
            #it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]

            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        #newlist is now the sorted version of lst! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.

        return newlist

print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

