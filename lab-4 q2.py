
# Step 1: Input multiple integers and create a list using list comprehension
numbers = [int(x) for x in input("Enter multiple integers separated by space: ").split()]

# Step 2: Calculate the mean
mean = sum(numbers) / len(numbers)

# Step 3: Calculate the median
numbers_sorted = sorted(numbers)
n = len(numbers)

if n % 2 == 0:
    # If even, median is the average of the two middle elements
    median = (numbers_sorted[n//2 - 1] + numbers_sorted[n//2]) / 2
else:
    # If odd, median is the middle element
    median = numbers_sorted[n//2]

# Step 4: Calculate the mode (most frequent element)
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Finding the number with the highest frequency
max_frequency = max(frequency.values())
mode = [key for key, value in frequency.items() if value == max_frequency]

# If there is more than one mode, pick the smallest one
mode = min(mode)

# Output the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
