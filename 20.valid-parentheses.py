# Here is a Python implementation of the solution to the "Valid Parentheses" problem:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        h = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in h.values():
                stack.append(c)
            elif not stack or stack.pop() != h[c]:
                return False
        return not stack

