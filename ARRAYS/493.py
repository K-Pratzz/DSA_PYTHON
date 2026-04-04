import bisect

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        lst = []
        ans = 0
        for x in nums:
            idx = bisect.bisect_right(lst, 2 * x)
            ans += len(lst) - idx
            bisect.insort(lst, x)
        return ans