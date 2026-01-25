'''Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.'''

nums=[int(x) for x  in input("Enter the list of numbers :").split()]
seen=set()
def conatins_duplicate(nums):

    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
print(conatins_duplicate(nums))
    