class Solution:
    def partition(self, s: str):
        result=[]
        def isPal(substr):
            left,right=0,len(substr)-1
            while left<right:
                if substr[left]!=substr[right]:
                    return False
                left+=1
                right-=1
            return True
        def backtrack(start,current):
            if start==len(s):
                result.append(list(current))
                return
            for end in range(start+1,len(s)+1):
                substr=s[start:end]
                if isPal(substr):
                    current.append(substr)
                    backtrack(end,current)
                    current.pop()      
        backtrack(0,[])
        return result
