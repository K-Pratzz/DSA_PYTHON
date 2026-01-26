'''Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2'''

nums=[int(x) for x in input("enter digits :").split()]
print(nums)
def missing_num(nums):
    n=len(nums)
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expected_sum-actual_sum

print(missing_num(nums))