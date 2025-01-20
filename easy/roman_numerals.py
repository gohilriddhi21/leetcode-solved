class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total = 0
        for i in range(len(s) - 1):
            print(s[i], s[i+1])
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                total = total - roman_numerals[s[i]]
            else:
                total = total + roman_numerals[s[i]]
            print(total)
        total = total + roman_numerals[s[-1]]
        return total

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("VI"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))