'''Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]'''

#counter={val:freq}
from collections import Counter
nums=[int(x) for x in input("enter no :").split()]
k=int(input("enter k : "))
def freq(nums,k):
    x=Counter(nums)
    freq=x.most_common(k)
    return [item[0] for item in freq]
print(freq(nums,k))