'''Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true'''

nums=[int(x) for x in input("Enter the list of numbers : ").split()]
k=int(input("enter the value of k :"))
seen={}
def contains_duplicate(nums,k):
    for indx, val in enumerate(nums):
        if val in seen and abs(indx-seen[val])<=k:
            return True
        seen[val]=indx
    return False
print(contains_duplicate(nums,k))
