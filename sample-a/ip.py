def is_valid_ip(s):
    nums = s.split(".")
    if len(nums) != 4:
        return False

    for num in nums:
        if not num.isdigit():
            return False
        if int(num) < 0 or int(num) > 255:
            return False
        if num[0] == 0 and len(num) > 1:
            return False

    return True


# Driver code
s1 = "128.0.0.1"
s2 = "125.16.100.1"
s3 = "125.512.100.1"
s4 = "125.512.100.abc"

print("Valid" if is_valid_ip(s1) else "Not valid")
print("Valid" if is_valid_ip(s2) else "Not valid")
print("Valid" if is_valid_ip(s3) else "Not valid")
print("Valid" if is_valid_ip(s4) else "Not valid")
