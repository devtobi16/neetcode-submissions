class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        r = 1
        l = 0
        prev = ""
        result = 1
        while r < len(arr):
            print(arr[r], result)
            if arr[r-1] < arr[r] and prev != "<":
                prev = "<"
                result = max(result, r - l + 1)
                r += 1
            elif arr[r-1] > arr[r] and prev != ">":
                prev = ">"
                result = max(result, r - l + 1)
                r += 1
            else:
            
                if arr[r-1] == arr[r]:
                    l = r
                    r += 1
                l = r - 1
                prev = ""
        return result




          
            


        