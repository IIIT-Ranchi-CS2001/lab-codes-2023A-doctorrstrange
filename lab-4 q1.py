
sentence = input("enter :")

# Convert sentence to lowercase, split into words, and filter palindrome words
palindromes = [word for word in sentence.split() if word.lower() == word.lower()[::-1]]

# Output the number of palindrome words
print(len(palindromes))
