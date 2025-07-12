"""
Task: Print the first n numbers in the Fibonacci series using a loop.
Example:
Input: 5 → Output: 0 1 1 2 3

"""
n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
