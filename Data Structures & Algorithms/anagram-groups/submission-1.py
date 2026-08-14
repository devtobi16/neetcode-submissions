class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {};
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in obj:
                obj[''.join(sorted(strs[i]))].append(strs[i])
            else:
                obj[''.join(sorted(strs[i]))] = [strs[i]]
        return list(obj.values())