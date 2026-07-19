def binsearch(nums, l, r, target):
    """
    """
    if left > right:
        return -1
    
    m = (r - l) // 2 + 1
    mid_val = nums[m]
    if target == mid_val:
        return m
    if target < mid_val:
        return binsearch(nums, l, m-1, target)
    if target > mid_val:
        return binsearch(nums, m+1, r, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        mark the start and end of the list by a left and right pointer
        left = 0
        right = len(nums) -1
        mid_pos = (left + right) // 2
        Compare element at middle to target
        if mid == target:
            return target
        if target < mid => it is in the sublist to left of mid
        right = mid_pos - 1
        repeat
        if left > right:
            return -1
        """

        l = 0
        r = len(nums) - 1
        while l <= r:

            m = (r + l) // 2
            if target < nums[m]:
                r = m -1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return -1
