#Some useful things about tuples

####Assigning multiple values / 'Unpacking' tuples
#(the same can be done with lists) 

book = ("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8")

title, author, isbn = book

print(title)
print(author)
print(isbn)

####Retrieving multiple values from a function (the same can be done with lists)

def quotient_and_remainder(dividend, divisor):
    return (dividend // divisor, dividend % divisor)

my_dividend = 11
my_divisor = 4

(my_quotient, my_remainder) = quotient_and_remainder(my_dividend, my_divisor)

print("Quotient:", my_quotient)
print("Remainder:", my_remainder)

####Accessing values in tuples

my_tup[0]
my_tup[0][0]  #if nested

