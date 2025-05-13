#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # You need to decrement n to avoid an infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <non-negative integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
    except ValueError:
        print("Error: Please enter a valid integer.")
        sys.exit(1)

    f = factorial(n)
    print(f)

