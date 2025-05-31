def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both inputs are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")
    
    # Check for division by zero
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    # Check divisibility
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
print(check_divisibility(10, 2))  # Output: True (10 is divisible by 2)
print(check_divisibility(7, 3))   # Output: False (7 is not divisible by 3)
