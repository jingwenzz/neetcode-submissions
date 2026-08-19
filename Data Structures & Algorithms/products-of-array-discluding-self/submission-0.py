class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0] * l
        suffix = [0] * l
        result = [0] * l

        for i in range(l):
            if i == 0:
                prefix[i] = 1
                continue
            
            prod_pre = nums[i-1] * prefix[i-1]
            prefix[i] = prod_pre

        for j in range(l-1, -1, -1):
            if j == l-1:
                suffix[j] = 1
                continue
            prod_suff = nums[j+1] * suffix[j+1]
            suffix[j] = prod_suff

        for k in range(l):
            result[k] = prefix[k] * suffix[k]

        return result

            

