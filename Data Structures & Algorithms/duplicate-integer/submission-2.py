import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_unique = len(np.unique(nums))
        if n_unique < len(nums): 
            return True
        else:
            return False
        