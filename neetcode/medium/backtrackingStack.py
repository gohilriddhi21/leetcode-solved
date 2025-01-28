class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            print("Open: ", openN, "Closed: ", closedN)
            print("Stack: ", stack)
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                print("Stack after pop: ", stack)

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
    
    def generateParenthesis_dp(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            print("\nK: ", k)
            for i in range(k):
                print("\ti: ", i)
                for left in res[i]:
                    print("\t\tleft: ", left)
                    for right in res[k-i-1]:
                        res[k].append(f"({left}){right}")
                        print("\t\t\tres: ",res)
        return res[-1]

if __name__ ==  "__main__":
    print(Solution().generateParenthesis_dp(3)) # ["((()))","(()())","(())()","()(())","()()()"]