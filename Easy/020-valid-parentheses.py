class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in lookup:
                stack.append(p)
            elif stack == [] or lookup[stack.pop()] != p:
                return False
        return stack == []


if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}"))
