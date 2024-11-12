# Input: Get the number from the user
num = int(input("Enter a number: "))

# Initialize variables
original_num = num
sum_of_digits = 0

# While loop to calculate the sum of digits
while num > 0:
    digit = num % 10       # Get the last digit
    sum_of_digits += digit # Add the digit to the sum
    num = num // 10        # Remove the last digit

# Output the result
print(f"The number is: {original_num}")
print(f"The sum of the digits is: {sum_of_digits}")
