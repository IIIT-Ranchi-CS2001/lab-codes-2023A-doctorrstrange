import math

# Function to find the roots of the quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        # One real repeated root
        root = -b / (2 * a)
        return (root, root)
    else:
        # Two complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Main function to take input and display roots
def main():
    # Taking input from the user
    a = int(input("Enter coefficient a (not equal to 0): "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return

    # Finding the roots
    roots = find_roots(a, b, c)

    # Displaying the roots
    if all(isinstance(root, complex) for root in roots):
        print(f"The roots are complex: {roots[0]} and {roots[1]}")
    else:
        print(f"The roots are: {roots[0]} and {roots[1]}")

# Running the main function
if __name__ == "__main__":
    main()
