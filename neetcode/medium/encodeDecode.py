class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + string + "#"
        return encoded[:-1]


    def decode(self, s: str) -> list[str]:
        res = s.split("#")
        return res

if __name__ == "__main__":
    strs = ["a","b","c"]
    solution = Solution()
    print(solution.encode(strs))
    print(solution.decode(solution.encode(strs)))