# Check if given number is a palindrome

num1 = 121
num2 = 542

def palindrome(num):
    
    input_num = num
    last_digit = 0
    reversed_num = 0
    
    while input_num > 0:
        
        last_digit = input_num % 10
        reversed_num = reversed_num * 10 + last_digit
        input_num = input_num // 10
        
    return num == reversed_num

print(palindrome(num1))
print(palindrome(num2))