d1 = {1:'a', 2:'b', 'c':3, 'd':None}

d2 = {'c':4, 'k':9, 'd':12}

# Accumulating all keys
all_keys = list(d1.keys()) + list(d2.keys()) 
final_dict = dict()

# Iterating through all unique keys
for unique_key in set(all_keys):

    # Getting values from first dictionary using unique key
    d1_values = d1.get(unique_key, [])
    if type(d1_values) is not list:
        d1_values = [d1_values]
    
    # Getting values from second dictionary using unique key
    d2_values = d2.get(unique_key, [])
    if type(d2_values) is not list:
        d2_values = [d2_values]

    # Concatenating values from both lists
    final_values = d1_values + d2_values

    # Getting first value if the list doesn't contain more than 1 elem
    # For printing purposes only (Optional)
    if len(final_values) < 2:
        final_values = final_values[0]

    final_dict[unique_key] = final_values

# Final output
print(final_dict)