'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3'''

nums=[int(x) for x in input("enter the list of numbers :").split()]
def majority(nums):
    count=0
    candidATE=None
    for num in nums:
        if count==0:
            candidATE=num
        if num==candidATE:
            count+=1
        else:
            count-=1
    return candidATE


#if it doesnt exist then 

if nums.count(majority(nums))>len(nums)//2:
    print(majority(nums))
else:
    print("no majority")
