class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(i):
            result.append(subset.copy())
            for num in range(i, len(nums)):
                subset.append(nums[num])
                backtrack(num+1)
                subset.pop()
        backtrack(0)
        return result
        

        