class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        def backtrack(start, sumVal):
            if sumVal == target:
                result.append(subset.copy())
                return
            for i in range(start, -1, -1):
                if sumVal < target:
                    subset.append(nums[i])
                    sumVal += nums[i]
                    backtrack(i, sumVal)
                    el = subset.pop()
                    sumVal -= el
                    
                
        backtrack(len(nums)-1,0)
        return result
