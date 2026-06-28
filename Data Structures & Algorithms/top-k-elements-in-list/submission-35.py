"""
List of lists can be sorted.
where the sublists are numbers, the sorting first checks the 1st elements of each sublists
ties are broken by checking the 2nd element and so on.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = defaultdict(int)
        n_dict = defaultdict(int)
        
        # {<num>: <count>,...}
        for el in nums:
            f_dict[el] += 1
        
        # {<count>: <num>}
        res = []
        for key, val in f_dict.items():
            res.append([val, key])  # list of [count, val]
        res_rev = sorted(res)[::-1]  # ascending order, compares 1st elements of sublists
        # print(res_rev)

        # now take k elements from the last
        out_list = []
        for i in range(k):
            out_list.append(res_rev[i][1])
            # print(out_list)
        
        return out_list

        