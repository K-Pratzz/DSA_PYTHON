class Solution:
    def combinationSum(self, candidates: int, target: int) :
        result=[]
        def backtrack(index,current,remaining):
            if remaining==0:
                result.append(list(current))
                return
            if index>=len(candidates) or remaining<0:
                return
            current.append(candidates[index])
            backtrack(index,current,remaining-candidates[index])
            current.pop()
            backtrack(index+1,current,remaining)
        backtrack(0,[],target)
        return result