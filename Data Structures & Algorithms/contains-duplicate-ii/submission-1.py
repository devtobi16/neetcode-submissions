class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for r in range(len(nums)):
            num = nums[r]
            if num in hashMap:
                if r - hashMap[num] <= k:
                    return True
            hashMap[num] = r
        return False

        