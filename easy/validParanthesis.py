class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if not stack or pairs[stack.pop()] != char:
                    return False
        return not stack
    
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("]"))
    print(s.isValid("["))
    print(s.isValid(")(){\}"))