# Input: Get the value of n
n = int(input("Enter the value of n: "))

# Header for the output
print("Number\tSquare")

# Initialize the starting number
i = 1

# While loop to calculate and display the squares
while i <= n:
    print(f"{i}\t{i**2}")
    i += 1
