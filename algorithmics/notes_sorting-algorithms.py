#SORTING-ALGORITHMS---------------------------------------------------------------|
#Algorithms that take as input a list and produce as output a sorted version of
#that list. Examples include: bubble sort, insertion sort, merge sort, shell sort,
#quick sort and heap sort.

#Bubble sort, O(n^2) -------------------------------------------------------------
#Compares each n and n+1 element and move them during a single iteration.

def sort_with_bubbles(lst):
    swap_occurred = True

    while swap_occurred:

        swap_occurred = False        

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:                
                temp = lst[i]           #just hold my lst[i] for a second!
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                swap_occurred = True

    return lst

#Note: after each iteration, the highest unsorted number should be moved to its
#appropriate posistion. There might be mulitple swaps during a single iteration.

print(sort_with_bubbles([4, 3, 5, 2, 1]))

#Selection sort, O(n^2)-----------------------------------------------------------
#Goes through the list, finds the lowest of the first item and moves it to the
#beginning. It then repeats the process, starting at the second item.

def sort_with_select(a_list):
    
    for i in range(len(a_list)):
        
        minIndex = i

        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[minIndex]:
                minIndex = j

        minValue = a_list[minIndex]  #just hold a_list[minIndex] for a second,
        del a_list[minIndex]         #until I delete it from its position
        a_list.insert(i, minValue)   #and insert at the correct one!
    
    return a_list

print(sort_with_select([5, 3, 1, 2, 4]))

#Merge sort, n log(n) ------------------------------------------------------------
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    else:
        midpoint = len(lst) // 2
        left = mergesort(lst[:midpoint])
        right = mergesort(lst[midpoint:])

        newlist = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            else:
                newlist.append(right[0])
                del right[0]

        newlist.extend(left)
        newlist.extend(right)

        return newlist

print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))


#Merge sort with PRINTS, n log(n) ------------------------------------------------
def mergesort(lst):
    
    if len(lst) <= 1:
        print("Returning one-item list:", lst)
        return lst
    else:
        midpoint = len(lst) // 2
        
        unsortedleft = lst[:midpoint]
        unsortedright = lst[midpoint:]
        
        print("Sorting left:", unsortedleft)
        left = mergesort(lst[:midpoint])
        print("Left sorted:", left)

        print("Sorting right:", unsortedright)
        right = mergesort(lst[midpoint:])
        print("Right sorted:", right)

        print("Merging", left, "and", right)
        newlist = []
        
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            else:
                newlist.append(right[0])
                del right[0]

        newlist.extend(left)
        newlist.extend(right)

        print("Returning merged list:", newlist)
        return newlist

print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))


#Merge sort with COMMENTS, n log(n) ----------------------------------------------
#Breaks the list into individual items, merge two adjacent lists and compares the
#lowest item in each. Whichever is lower, is added to the new list.

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

