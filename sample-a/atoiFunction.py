def myAtoi(s):
    s = s.strip()  # 1. Remove leading/trailing whitespace
    sign = 1       # 2. Initialize sign (1 for positive, -1 for negative)
    result = 0     # 3. Initialize result
    index = 0      # 4. Initialize index
    INT_MAX = 2**31 - 1  # 5. Define max int value
    INT_MIN = -2**31   # 6. Define min int value

    if index < len(s) and s[index] == '-':  # 7. Check for negative sign
        sign = -1
        index += 1
    elif index < len(s) and s[index] == '+':  # 8. Check for positive sign
        index += 1

    while index < len(s) and s[index].isdigit():  # 9. Iterate through digits
        digit = int(s[index])  # 10. Convert current char to digit

        # 11. Overflow check
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN  # 12. Return max/min int

        result = result * 10 + digit  # 13. Build the integer
        index += 1

    return sign * result  # 14. Return the signed result

s = " -91283472332"
print(myAtoi(s))