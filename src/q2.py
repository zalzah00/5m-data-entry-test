def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Create a new list with replaced values
    return [replace_val if x == find_val else x for x in lst]

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))  # Output: [1, 5, 3, 4, 5, 5]
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))  # Output: ["orange", "banana", "orange"]
