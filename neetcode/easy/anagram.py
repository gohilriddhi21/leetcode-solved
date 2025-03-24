class Solution:
    # Time complexity: O(n log n + m log m)
    def sortingAnagram(self, s: str, t: str) -> bool:
        return False if len(s) != len(t) else sorted(s) == sorted(t)
    
    # Time complexity: O(n^2)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return all(s.count(char) == t.count(char) for char in s)
    
    # Time complexity: O(n)
    def trying(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        for i in range(len(countS)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
    # Time complexity: O(n)
    def hashtableAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            print(f"{s[i]} s: ",ord(s[i]), ord('a'))
            count[ord(s[i]) - ord('a')] += 1

            print(f"{t[i]} t: ",ord(t[i]), ord('a'))
            count[ord(t[i]) - ord('a')] -= 1
            print(count)

        return all(val == 0 for val in count)

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))  # True
    print(Solution().hashtableAnagram("anagram", "nagaram"))  # True
    print(Solution().trying("anagram", "nagaram"))  # True
