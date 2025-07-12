"""
Task: Take a string as input and print its reverse using a loop.
Example:
Input: "hello" → Output: "olleh"

"""

input_string = input("Enter a string: ")

reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)

