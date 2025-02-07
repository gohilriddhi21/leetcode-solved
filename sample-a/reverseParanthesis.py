class Solution:
    def paranthesisCheck(self, value):
        opened = 0
        closed = 0

        for char in value:
            if char == '(':
                opened+=1
            elif char == ')':
                closed+=1
        return opened == closed


if __name__ == "__main__":
    print(Solution().paranthesisCheck("())()("))