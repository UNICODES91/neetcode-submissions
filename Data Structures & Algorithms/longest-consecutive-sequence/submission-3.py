class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. sort ascending - leaves elements in order
        2. loop over each in sorted array and count consecutive
        3. when consecutive breaks, save count, start new count with next element
        """
        nums = sorted(nums)
        # print(nums)
        if len(nums) < 1:
            return 0
        
        counts = []
        last_num = nums[0]
        curr_count = 1
        for el in nums:
            if el == last_num:
                continue
            elif el - last_num == 1:
                curr_count += 1
            else:
                counts.append(curr_count)
                curr_count = 1
            last_num = el
            # print(f"el = {el}, last_num = {last_num}, curr_count = {curr_count}, counts = {counts}")
        counts.append(curr_count)
        # print(counts)
        return max(counts)



            
