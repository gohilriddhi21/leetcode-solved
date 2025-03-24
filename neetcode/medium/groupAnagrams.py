from collections import defaultdict
class Solution:
    # Time complexity: O(m * n log n)
    # sorting takes n log n
    # m is the length of the input list
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cnt = defaultdict(list)
        for s in strs:
            cnt["".join(sorted(s))].append(s)
        return list(cnt.values())
    
    # Time complexity: O(m * n)
    def groupAnagrams_2(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        # for each string in strs
        for s in strs:
            count = [0] * 26
            # for each character in the string get the cnt[0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()


if __name__ == "__main__":
    print(Solution().groupAnagrams_2(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]