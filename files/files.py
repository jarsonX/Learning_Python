#FILE MODES
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

#WRITING FILES
#Overwrites a file

file_1: str = r"C:\Users\krzys\Downloads\Example1.txt"
file_2: str = r"C:\Users\krzys\Downloads\Example2.txt"

with open(file_2, "w") as writefile:
    writefile.write("This is line A in file 2\n")
    writefile.write("This is line B in file 2\n")
    writefile.write("This is line C in file 2\n")
    
#WRITING FROM A LIST
#Overwrites a file

lines_to_write = ["This is the beginning\n", "This is the middle\n", "And this is the end\n"]

with open(file_2, "w") as writefile:
    for line in lines_to_write:
        writefile.write(line)
        
#APPENDING FILES
#Do not overwrite a file

with open(file_2, "a") as appendfile:
    appendfile.write("The lines continue\n")
    appendfile.write("And they continue like a lot!\n")
    
#COPYING A FILE
    
with open(file_1, "r") as readfile:
    with open(file_2, "w") as writefile:
        for line in readfile:
            writefile.write(line)
