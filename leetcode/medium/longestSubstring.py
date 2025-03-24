class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = j = max_len = 0
        seen = set()
        
        while(i < n):
            while seen and s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            max_len = max(max_len, i - j + 1)
            i += 1    
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
