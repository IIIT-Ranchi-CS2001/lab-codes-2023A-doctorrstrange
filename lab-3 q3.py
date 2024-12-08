# Input: Get the value of n
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Initialize a counter to track the number of terms printed
count = 0

# While loop to generate and print Fibonacci numbers
print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    # Update the values of a and b for the next term
    a, b = b, a + b
    count += 1
