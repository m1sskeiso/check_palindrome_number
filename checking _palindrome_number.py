# Defining a function for checking a palindrome number
def is_palindrome(number):
# Convert the number to a string for easy comparison   
        str_number = str(number)

# Check if the string is the same when reversed
        return str_number == str_number[::-1]

# Test cases
number1 = 545
number2 = 12321

print(f"{number1} is a palindrome: {is_palindrome(number1)}")
print(f"{number2} is a palindrome: {is_palindrome(number2)}")

