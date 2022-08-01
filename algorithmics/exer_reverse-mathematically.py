# Reverse a number mathematically

num = 12345

def reverse(num):
    
    input_num = num
    last_digit = 0
    reversed_num = 0
    
    while input_num > 0:
        
        last_digit = input_num % 10
        reversed_num = reversed_num * 10 + last_digit
        input_num = input_num // 10
        
    return reversed_num

print(reverse(num))