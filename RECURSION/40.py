class Solution:
    def combinationSum2(self, candidates: int, target: int):
        result = []
        # 1. Sort to bring duplicates together and allow early tracking/pruning
        candidates.sort()
        
        def backtrack(index, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            if remaining < 0:
                return
            
            # 2. Iterate through candidates starting from the current index
            for i in range(index, len(candidates)):
                # 3. Skip duplicates: if this element is the same as the previous 
                # element in this loop, skip it to prevent duplicate combinations.
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(candidates[i])
                # Move to 'i + 1' because we cannot reuse the exact same element
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop() # Backtrack

        backtrack(0, [], target)
        return result