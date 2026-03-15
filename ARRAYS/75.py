class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=one=two=0
        for x in nums:
            if x ==0:zero+=1
            elif x==1:one+=1
            else:two+=1

        for i in range(zero):
            nums[i]=0
        for j in range(zero,zero+one):
            nums[j]=1
        for k in range(zero+one,zero+one+two):
            nums[k]=2
