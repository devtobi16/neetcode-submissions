class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        r = 0
        l = 0
        sumVal = 0
        currMin = 0
        while r < len(nums):
            num = nums[r]
            sumVal += num
            while sumVal >= target:
                result = min(result, r - l + 1)
                sumVal -= nums[l]
                l += 1
            r += 1
        
        return result if result < float('inf') else 0
        