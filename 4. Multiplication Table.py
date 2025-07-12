"""
Task: Take a number as input and print its multiplication table up to 10.
Example:
Input: 5 →

"""
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
