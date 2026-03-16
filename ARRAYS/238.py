class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        prefix=1
        for x in range(n):
            ans[x]=prefix
            prefix*=nums[x]
        suffix=1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans