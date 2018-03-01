class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, j in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != j:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["hello", "heaven", "heavy"]))
