class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_count = 0
        for i, el in enumerate(nums):
            if el == 0:
                if counter > max_count:
                    max_count = counter
                counter = 0
            else:
                counter += 1
                
        if counter > max_count:
            max_count = counter
        return max_count




        