# Input: Get the string and the character to search for
text = input("Enter a string: ")
char_to_find = input("Enter the character to find: ")

# Initialize a counter for occurrences
count = 0

# Loop through each character in the string
for char in text:
    if char == char_to_find:
        count += 1

# Output the result
print(f"The character '{char_to_find}' occurs {count} times in the given string.")
