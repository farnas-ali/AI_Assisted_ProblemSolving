def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
        n (int): The number to compute the factorial for.

    Returns:
        int: The factorial of n if n is non-negative.
        str: Error message if n is negative.
    """

    # Check for negative input
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."

    # Factorial of 0 is always 1
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage:
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(-4))  # Error message
