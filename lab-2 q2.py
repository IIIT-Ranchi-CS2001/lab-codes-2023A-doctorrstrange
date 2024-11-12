# Given string
S = "Ba Ba Black Sheep"

# 1. The length of the string S
length_of_S = len(S)

# 2. The first occurrence of the letter 'e'
first_occurrence_e = S.find('e')

# 3. The total number of occurrences of 'a'
total_occurrences_a = S.lower().count('a')

# 4. Generate "Ta Ta Black Sheep"
new_string = S.replace("Ba", "Ta")

# Displaying the results
print("Length of S:", length_of_S)
print("First occurrence of 'e':", first_occurrence_e)
print("Total occurrences of 'a':", total_occurrences_a)
print("Generated string:", new_string)
