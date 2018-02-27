class Solution(object):

    def isPalindrome(self, x):
        if x < 0:
            return False
        copy = x
        reverse = 0
        while copy:
            reverse = reverse * 10 + copy % 10
            copy //= 10

        return x == reverse


if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)
