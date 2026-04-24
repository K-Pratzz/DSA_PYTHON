class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            curr=arr[i]
            if curr>arr[i-1] and curr>arr[i+1]:
                return i