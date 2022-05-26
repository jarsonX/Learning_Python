#FILE MODS
##############################################################################
# r - read
# r+ - read and write, cannot truncate
# w - write, cursor at the beginning
# w+ - write and read, can truncate
# a - append, cursor at the end
# a+ - append and read, creates a new file, if none exists

# .tell() - returns the current position (of "cursor") in bytes
# .seek(offset, from) - changes the position by "offset" bytes with respect to
# from. "From" can take the valu eof 0, 1, 2 corresponding to beginning,
# relative to current position and end.

#EASY WAY TO STORE LOCATION OF A FILE
##############################################################################
file_1: str = r"C:\Users\krzys\Downloads\Example1.txt"
file_2: str = r"C:\Users\krzys\Downloads\Example2.txt"

#READING FILES
##############################################################################
inputfile = open(file_1, "r")

#READLINE
#####################
inputfile.readline()  #read the current line and stop at the beginning of the next line
inputfile.readline()  #read the next line and stop at the beginning of the next line
print(inputfile.readline().strip())  #strip is to remove \n and avoid additional, blank line

#LOADING INTO LISTS
#####################
my_list = []
inputfile = open(file_1, "r")

for line in inputfile:
    my_list.append(line.strip())

#WRITING FILES
##############################################################################
#Overwrites a file

with open(file_2, "w") as writefile:
    writefile.write("This is line A in file 2\n")
    writefile.write("This is line B in file 2\n")
    writefile.write("This is line C in file 2\n")
    
#WRITING FROM A LIST
#####################
#Overwrites a file
#.write can only write strings

lines_to_write = ["This is the beginning\n", "This is the middle\n", "And this is the end\n"]

with open(file_2, "w") as writefile:
    for line in lines_to_write:
        writefile.write(line)

#WRITELINES METHOD
#####################
lines_to_write = ['ABC', 'DEF', 'GHJ']

with open(file_2, 'w') as writefile:
    writefile.writelines(lines_to_write)  #writes all els in the same line
    
with open(file_2, 'w') as writefile:   
    writefile.write('\n'.join(lines_to_write))  #so this is more useful

#WRITE USING PRINT
#####################
lines_to_write = ['ABC', 'DEF', 'GHJ']

writefile = open(file_2, 'w')

for el in lines_to_write:
    print(name, file = writefile)  #automatically prints each in a new line

#APPENDING FILES
##############################################################################
#Do not overwrite a file

with open(file_2, "a") as appendfile:
    appendfile.write("The lines continue\n")
    appendfile.write("And they continue like a lot!\n")
    
#COPYING A FILE
##############################################################################
    
with open(file_1, "r") as readfile:
    with open(file_2, "w") as writefile:
        for line in readfile:
            writefile.write(line)
            
#SAVE AND LOAD FUNCTIONS
##############################################################################

#Saves in_list to the file
def save(filename, in_list):
    outputfile = open(filename, "w")
    
    for item in in_list:
        print(item, file = outputfile)
        
    outputfile.close()
    
#Loads from filename and returns a list of the contents
def load(filename):
    inputfile = open(filename, "r")
    in_list = []
    
    for line in inputfile:
        in_list.append(line.strip())
    
    inputfile.close()
    return in_list

#Example
my_list = ['ABC', 'BCD']
save("file_sample_01.txt", my_list)
new_list = load("file_sample_01.txt")
print(new_list)
