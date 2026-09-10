class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        result = 0
        r = 0
        l = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        return result
            
        