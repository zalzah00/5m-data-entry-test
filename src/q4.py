def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Reverse the string using slicing
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
print(string_reverse("Hello World"))  # Output: "dlroW olleH"
print(string_reverse("Python"))       # Output: "nohtyP"
