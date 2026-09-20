class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        visited = set()
        subset = []
        def backtrack(i):
            if tuple(subset) not in visited:
                result.append(subset.copy())
                visited.add(tuple(subset))
            for num in range(i, len(nums)):
                subset.append(nums[num])
                backtrack(num+1)
                subset.pop()
        backtrack(0)
        return result




        