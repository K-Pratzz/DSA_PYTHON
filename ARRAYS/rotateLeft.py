nums=[int(x) for x in input("enter numbers : ").split()]
def rotateLeft(nums):
    if len(nums)==0:
        return []
    first =nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[-1]=first
    return nums
    
print(rotateLeft(nums))