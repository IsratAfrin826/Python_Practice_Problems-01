"""
2. Count Vowels
Task: Take a string and count the number of vowels (a, e, i, o, u).
Example:
Input: "sunny" → Output: 1

"""

input_string = input("Enter a string: ")

vowels = "aeiouAEIOU"

count = 0

for char in input_string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
