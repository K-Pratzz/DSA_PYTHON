'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].'''

nums=(int(x) for x in input("enter the list of numbers : ").split())
def running_sum(nums):
    run_sum=[]
    curr_sum=0
    for x in nums:
        curr_sum+=x
        run_sum.append(curr_sum)
    return run_sum
print(running_sum(nums))