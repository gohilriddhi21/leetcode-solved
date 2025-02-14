class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1: At some point both will become same
        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = sum(int(digit) ** 2 for digit in str(n))  # Sum of squares of digits
        # return n == 1

        
        # 2: Floyd's fast and slow runner
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


print(Solution().isHappy(19))