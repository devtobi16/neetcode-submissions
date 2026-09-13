class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        i = 0
        j = 0
        result = 0
        maxFreq = 0
        while j < len(s):
            hashMap[s[j]]= hashMap.get(s[j], 0) + 1
            maxFreq = max(hashMap[s[j]], maxFreq)
            while (j - i + 1) - maxFreq > k:
                hashMap[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
            j += 1
        return result
