class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_left, max_right = 0, 0
        water = 0

        while l < r:
            max_left = max(height[l], max_left)
            max_right = max(height[r], max_right)

            if max_left < max_right:
                water += max_left - height[l]
                l += 1
            else:
                water += max_right - height[r]
                r -= 1

        return water