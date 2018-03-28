class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # zip()-用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map = {}
        map_val = set()
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            elif t[i] in map_val:
                return False
            else:
                hash_map[s[i]] = t[i]
                map_val.add(t[i])
        return True
