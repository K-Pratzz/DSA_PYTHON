'''Given an unsorted array of integers nums, return the length of the longest consecutive elements
 sequence.You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.'''

nums=set([int(x) for x in input("enter no :").split()])


def seq(nums):
    long=0
    for x in nums:
        if (x-1) not in nums:
            current=x
            length=1
            while current+1 in nums:
                length+=1
                current+=1
            long=max(length,long)
    return long

print(seq(nums))