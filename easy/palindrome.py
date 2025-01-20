class Solution(object):
    def is_Palindrome_by_mod(self, x):
        """
        Checks if a number is a palindrome by reversing the number without converting the number to string.
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original_number = x
        new_no = 0
        
        while x>0:
            new_no = new_no * 10 + x % 10
            x //= 10 # so that it doesn't run infinitely or rather new_no is never inf
        return original_number == new_no

    
    # Best solution
    def is_Palindrome_by_half(self, x):
        """
        Divides half the number, reverses the second half then compares the two halves.
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        
        y = 0
        while x > y:
            y = (y * 10) + (x % 10)
            x //= 10
        
        return x == y or x == y // 10
        
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.is_Palindrome_by_mod(0))
    print(s.is_Palindrome_by_mod(121))
    print(s.is_Palindrome_by_mod(-121))
    print(s.is_Palindrome_by_mod(10))
    print(s.is_Palindrome_by_mod(99))
    
    print(s.is_Palindrome_by_half(12321))
    print(s.is_Palindrome_by_half(121))
