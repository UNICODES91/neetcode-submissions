class Solution:
    """
    Create a result list filled with zeros.
    Use a stack to store pairs of (temperature, index) for days that haven't found a warmer day yet.
    Iterate through the temperature list:
        While the stack is not empty and the current temperature is warmer than the top of the stack:
            Pop the top element.
            Compute how many days passed and update the result.
        Push the current day onto the stack.
    Return the filled result list.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res