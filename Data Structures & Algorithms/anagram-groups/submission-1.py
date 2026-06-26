class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a default dict that has values of list type
        # avoids having to check for existence of keys manually
        anagram_dict = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
            # if sorted_s in anagram_dict:
                # anagram_dict[sorted_s].append(s)
            # else:
                # anagram_dict[sorted_s] = [s]
        
        res = list(anagram_dict.values())
        # print(list(anagram_dict.values()))
        # out_list = []
        # for i, s in enumerate(strs):
        #     l = [s]
        #     for t in strs[i+1:]:
        #         if self.is_anagram(s, t):
        #             l.append(t)
        #             strs.remove(t)
        #     out_list.append(l)
        return res


    def is_anagram(self, str1, str2):
        """
        Returns true is str2 is anagram of str1
        """
        if len(str1) != len(str2):
            return False

        dict1 = {}
        dict2 = {}
        for ch1, ch2 in zip(str1, str2):
            if ch1 not in dict1:
                dict1[ch1] = 1
            else:
                dict1[ch1] += 1

            if ch2 not in dict2:
                dict2[ch2] = 1
            else:
                dict2[ch2] += 1
        return dict1 == dict2

        