import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        push elements to stack till operator found
        if operator, pop 2 from stack and do:
            el2 <op> <el1>
            push result to stack
        return final stack value as result
        """
        ops = {'+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv}
        
        stack = []
        for el in tokens:
            if el in ops.keys():
                op1 = stack.pop()
                op2 = stack.pop()
                res = int(ops[el](op2, op1))
                stack.append(res)
                # print(stack)
            else:
                stack.append(int(el))
        res = stack.pop()
        return res


        