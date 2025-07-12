"""
Task: Take a number and calculate the sum of its digits using a loop.
Example:
Input: 1234 → Output: 10

"""
number = input("Enter a number: ")

total = 0

for digit in number:
    total += int(digit)

print("Sum of digits:", total)
