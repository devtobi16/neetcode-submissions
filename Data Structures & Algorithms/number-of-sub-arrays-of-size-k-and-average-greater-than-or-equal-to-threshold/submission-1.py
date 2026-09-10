class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        l = 0
        sumVal = 0
        r = 0
        while r < len(arr):
            sumVal += arr[r]
            if r - l + 1 == k:
                if sumVal / k >= threshold:
                    result += 1
                sumVal -= arr[l]
                l += 1
            r += 1
        return result
            

        