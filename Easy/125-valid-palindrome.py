class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c.lower())

        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[-(i + 1)]:
                return False

        return True

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_list = [c for c in s.lower() if c.isalnum()]
        return clean_list == clean_list[::-1]
