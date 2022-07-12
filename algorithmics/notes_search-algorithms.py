#-SEARCH-ALGORITHMS---------------------------------------------------------------------------------|

#Algorithms that take as input a list and a value for which to search, and produce as output the 
#index or indices where that  value was found in the list.

#Linear search, version 1, O(n) --------------------------------------------------------------------
def linear(lst, text):
    
    for i in enumerate(lst):
        if i[1] == text:
            return i[0]
    
    return False

a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))

#Linear search, version 2, O(n) --------------------------------------------------------------------
def linear(a_list, an_item):
    
    for i in range(len(a_list)):
        if a_list[i] == an_item:
            return i       

    return False

a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
