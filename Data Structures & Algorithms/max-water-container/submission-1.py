class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0

        while l < r:
            l_hg, r_hg = heights[l], heights[r]
            length = r - l
            current_water = min(l_hg, r_hg) * length
            max_water = max(current_water, max_water)
            if l_hg < r_hg:
                l += 1
            else:
                r -= 1
        
        return max_water