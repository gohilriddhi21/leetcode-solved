def excel_column_name(n):
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26) 
        result = chr(65 + remainder) + result  
    return result

# Test cases
print(excel_column_name(1))   # Output: A
print(excel_column_name(2))   # Output: B
print(excel_column_name(26))  # Output: Z
print(excel_column_name(27))  # Output: AA
print(excel_column_name(52))  # Output: AZ
print(excel_column_name(702)) # Output: ZZ
print(excel_column_name(703)) # Output: AAA