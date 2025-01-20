class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest_word = min(strs, key=len) 

        for i, char in enumerate(shortest_word):
            for other_word in strs:
                if other_word[i] != char:
                    return shortest_word[:i]
        return shortest_word
            
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))