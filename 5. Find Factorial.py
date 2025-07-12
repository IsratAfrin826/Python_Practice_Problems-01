"""
Task: Write a program that calculates the factorial of a number using a loop.
Example:
Input: 5 → Output: 120

"""
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)
