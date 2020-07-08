https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, left, right = 0, 0, len(height)-1
        maxh = max(height)
        while left < right: 
            maxarea = max(maxarea, min(height[left], height[right]) * (right-left))
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
            if maxh * (right-left) < maxarea: return maxarea
        return maxarea
                
        
        