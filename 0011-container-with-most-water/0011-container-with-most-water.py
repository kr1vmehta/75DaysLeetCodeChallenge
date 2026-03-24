class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            # Calculate current area
            current_height = min(height[l], height[r])
            current_area = current_height * (r - l)
            max_area = max(max_area, current_area)
            
            # Move the pointer with the smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
