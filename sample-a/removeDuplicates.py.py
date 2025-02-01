def remove_duplicates(s):
    # Function to remove duplicate characters
    # Create a list to store frequency for ASCII characters
    ch = [0] * 256
    result = []

    # Traverse the input string
    for char in s:
        
        # Check if current character's frequency is 0
        if ch[ord(char)] == 0:
            
            # Add char if frequency is 0
            result.append(char)

            # Increment frequency
            ch[ord(char)] += 1
    
    return ''.join(result)

# Driver code
s = "geeksforgeeks"
print(remove_duplicates(s))