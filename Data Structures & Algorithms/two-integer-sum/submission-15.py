
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """
    #     Since there is only 1 pair of numbers that will give target,
    #     start with 1st element, subtract from target, get index of result
    #     if index found, stop, else move to next element
    #     """
    #     for pos, num in enumerate(nums):
    #         res = target - num
    #         try:
    #             ind = nums[pos + 1:].index(res)
    #         except:
    #             continue
    #         return [pos, ind+pos + 1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Alternative solution using dictionaries for better runtime efficiency
        """
        seen_dict = {}
        for pos, num in enumerate(nums):
            diff = target - num
            if diff not in seen_dict:
                seen_dict[num] = pos
            else:
                return [seen_dict[diff], pos]

            
