class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Pass 1:
        ---------
        Go from left to right and at each position, compute a running pre-term product: product of prev el.
        append running product of pre-terms to buffer

        Pass 2:
        -------
        GO from right to left, compute running product of elements after itself
        multiply with the existing buffer elements in prev step

        """
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
            

