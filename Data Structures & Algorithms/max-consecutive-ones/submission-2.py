class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        counts = []
        for i, el in enumerate(nums):
            if el == 0:
                counts.append(counter)
                counter = 0
            else:
                counter += 1
        counts.append(counter)
        return max(counts)




        