#DEFINITIONS
##############################################################################

#Dictionaries: A data structure comprised of key-value pairs, where a key is 
#entered into the dictionary to get out a value. Similar to or synonymous with 
#Maps, Associative Arrays, HashMaps, and Hashtables.

#Dictionary Key: A value then, when passed into a dictionary, returns 
#a corresponding value, like a word and its definition. Similar to a variable.

#Dictionary Value: A value returned in response to a key in a dictionary. 
#Similar to a value of a variable outside a dictionary.

#Note: keys must be immutable.

#USEFUL METHODS
##############################################################################

#values(): returns a list of all the values of that dictionary.
#keys(): returns a list of all the keys in that dictionary.
#items(): returns a list of (key, value) tuples in that dictionary.

#Above are important for loops, e.g. in order to get both a value and a key
#at the same time in loop, we should use 'for (key, value) in dict.items():'

#BASICS
##############################################################################

#Creating a dictionary
new_dict = {"Jarvis": 1250, "Leon": 300}

#Modifying values
new_dict["Jarvis"] += 350

#Adding values
new_dict["Mysza"] = 3000

#Removing values
del new_dict["Leon"]

print(new_dict)

#'in' operator checks KEYS, not values
if "Jarvis" in new_dict:
    print(new_dict["Jarvis"])  #prints value for Jarvis

#SORTING
##############################################################################    

dictionary = sorted(dictionary)
dictionary[key].sort()  #only if value is sortable (like a list)

#TRAVERSING DICTIONARIES
##############################################################################

#Iterating over values only
for value in new_dict.values():
    if value < 500:
        print("Value found:", value)

#Iterating over keys, approach 1
for key in new_dict.keys():
    value = new_dict[key]  #this can be done easier, see approach 2
    if value < 5:
        print(key, "is less than 500:", value)

#Iterating over keys, approach 2
for (key, value) in new_dict.items():
    if value < 5:
        print(key, "is less than 500:", value)

#PRINTING DICTIONARIES LINE BY LINE
##############################################################################
import json

dict_line_by_line = json.dumps(my_dictionary, indent=1)
print(dict_line_by_line)
