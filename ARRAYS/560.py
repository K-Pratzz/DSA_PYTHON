class Solution:
    def subarraySum(self, nums: int, k: int):
        maap={0:1}
        currSum=0
        count=0
        for x in nums:
            currSum+=x
            diff=currSum-k
            if diff in maap:
                count+=maap[diff]
            maap[currSum]=maap.get(currSum,0)+1
        return count