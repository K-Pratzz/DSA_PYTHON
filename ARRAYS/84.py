class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        maxarea=0
        stack=[-1]
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                maxarea=max(maxarea,h*w)
            stack.append(i)
        heights.pop()
        return maxarea
