class Solution:
    """
    ex: (([{}]))
    ( -> [(]
    ( -> [(, (]
    """
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")",
                        "{": "}",
                        "[":"]"}
        # if len(s) < 2:  # with just 2 char, cannot be valid string
        #     return False
        stack = []
        for ch in s:
            # if opening bracket, add to stack
            if ch in bracket_pairs.keys():
                stack.append(ch)
            
            # if a closing bracket, pop last stack element and match
            elif ch in bracket_pairs.values():
                # found closing even before a single starting
                if len(stack) == 0:
                    return False
                start = stack.pop(-1)
                if bracket_pairs[start] != ch:
                    return False
        if len(stack) > 0:
            return False
        return True