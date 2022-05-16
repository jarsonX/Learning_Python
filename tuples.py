#Some useful things about tuples

####Assigning multiple values (the same can be done with lists)

def unpack_and_reverse(a_tuple):
    (el_1, el_2, el_3) = a_tuple[0:3]
    return (el_3, el_2, el_1)

print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))


####Retrieving multiple values from a function (the same can be done with lists)

def quotient_and_remainder(dividend, divisor):
    return (dividend // divisor, dividend % divisor)

my_dividend = 11
my_divisor = 4

(my_quotient, my_remainder) = quotient_and_remainder(my_dividend, my_divisor)

print("Quotient:", my_quotient)
print("Remainder:", my_remainder)


