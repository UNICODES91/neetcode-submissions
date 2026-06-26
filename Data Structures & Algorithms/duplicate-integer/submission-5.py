import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out_list = []
        for el in nums:
            if el in out_list:
                return True
            else:
                out_list.append(el)
        return False
        