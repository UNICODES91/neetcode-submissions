class Solution:

    def encode(self, strs: List[str]) -> str:
        n_strs = len(strs)
        out = f"{n_strs:03d}"
        # print(out)
        # print(len(out))
        for s in strs:
            # print(s)
            # l = str(len(s))
            l = f"{len(s):03d}"
            out = out + l+ s
            # print(out)
        # print(out)
        return out

    def decode(self, s: str) -> List[str]:
        out_list = []
        # 1st 3 chars give number of strings
        n_strs = int(s[0:3])
        start_pos = 3
        l = len(s)
        while start_pos < l:
            # every substr. starts with 3 chars for it's length
            s_chars = int(s[start_pos: start_pos + 3])
            start_pos += 3
            sub_s = s[start_pos: start_pos + s_chars]
            out_list.append(sub_s)
            start_pos += s_chars

        return out_list
