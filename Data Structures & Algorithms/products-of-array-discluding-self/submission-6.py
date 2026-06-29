class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # p = 1
        for i, v in enumerate(nums):
            p = 1
            for j in range(0, i):
                p *= nums[j]
            
            for k in range(i+1, len(nums)):
                p *= nums[k]
            res.append(p)
        return res



        