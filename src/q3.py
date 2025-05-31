def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists
    if key in dct:
        print(f"Key '{key}' already exists with value: {dct[key]}")
    
    # Update or add the key-value pair
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
print(update_dictionary({}, "name", "Alice"))
# Output: {'name': 'Alice'}

print(update_dictionary({"age": 25}, "age", 26))
# Output: 
# Key 'age' already exists with value: 25
# {'age': 26}
