'''Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''

nums=[int(x) for x in input("enter the list of numbers :").split()]
print(nums)
target=int(input("enter the target value :"))

def two_sum(nums,target):
    map={} #val : indx
    for indx, val in enumerate(nums): #index and value
        diff=target-val
        if diff in map:
            return [map[diff],indx]
        map[val]=indx
    return []
print(two_sum(nums,target))