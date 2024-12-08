# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    # Check if the cleaned string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Main program
if __name__ == "__main__":
    # Enter any string at runtime
    user_input = input("Enter a string: ")
    
    # Check if the string is a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
