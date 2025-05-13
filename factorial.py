#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

# Check if a number is provided
if len(sys.argv) != 2:
    print("Usage: ./script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        sys.exit(1)
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

f = factorial(number)
print(f)

