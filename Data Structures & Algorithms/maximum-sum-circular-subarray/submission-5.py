class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        total = sum(nums)
        for i in range(1,len(nums)):
            currMax = max(nums[i], nums[i]+ currMax)
            currMin = min(nums[i], nums[i]+ currMin)
            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)
        print(globalMax,globalMin, total)
        if globalMax < 0:
            return globalMax
        else:
            return max(total - globalMin,globalMax)
        

        


        