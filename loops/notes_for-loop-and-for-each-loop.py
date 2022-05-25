#################################################
# For loop and For each loop 
#################################################

#For loop--------------------------

#for i in range(len(the_variable)):
 #   the_value = the_variable[i]
  #  …

mystery_string = “Jarson”

for x in range(len(mystery_string)):
    print(x, mystery_string[x])

# 0 J
# 1 a
# 2 r
# 3 s
# 4 o
# 5 n
    
#For each loop---------------------

#i = -1
#for the_value in the_variable:
 #   i += 1
  #  …

mystery_string = “Jarson”

i = 0
for x in mystery_string:
    print(i, x)
    i +=1

# 0 J
# 1 a
# 2 r
# 3 s
# 4 o
# 5 n

#################################################
#Enumerate
#################################################

squares = ["red", "yellow", "green"] 

for i, square in enumerate(squares): 
print(i, square)

#0 red
#1 yellow
#2 green

