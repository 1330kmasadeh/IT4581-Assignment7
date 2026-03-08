# recursive_functions.py
# Example recursive functions: factorial and fibonacci

def factorial(n):
    # base case
    if n == 1:
        return 1
    # recursive step
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    # base cases
    if n <= 1:
        return n
    # recursive step
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# test the functions
print("Factorial of 5:", factorial(5))
print("Fibonacci of 6:", fibonacci(6))
