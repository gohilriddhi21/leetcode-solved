class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))  # True
