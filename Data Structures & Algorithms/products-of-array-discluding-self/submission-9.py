class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        post = 1
        for i, n in enumerate(nums):
            if i > 0:
                pre *= nums[i-1]
            res.append(pre)
        
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                post *= nums[i+1]
            res[i] *= post
        # print(res)
        return res
            

