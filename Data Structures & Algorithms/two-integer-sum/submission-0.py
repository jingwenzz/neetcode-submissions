class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in d:
                return [d[need], i]
            d[n] = i
    