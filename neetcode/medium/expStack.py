class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        res = ""
        for t in tokens:
            if t not in ["+","-","/","*","%"]:
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                res = f"({a}{t}{b})"
                stack.append(int(eval(res)))
        return eval(str(stack[-1]))

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2","1","+","3","*"])) # 9
    print(s.evalRPN(["4","13","5","/","+"])) # 6