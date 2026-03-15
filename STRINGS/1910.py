class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ansStack=[]
        for x in s:
            ansStack.append(x)
            if len(ansStack)>=len(part) and "".join(ansStack[-len(part):])==part:
                for x in range(len(part)):
                    ansStack.pop()
        return "".join(ansStack)