class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

if __name__ == "__main__":
    strs = ["we","love","neetcode"]
    solution = Solution()
    print(solution.encode(strs))
    print(solution.decode(solution.encode(strs)))