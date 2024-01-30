class Solution(object):
    def isPalindrome(self, x):
        rev_num= str(x)[::-1]
        if (str(x) == rev_num):
            return True
        else:
            return False
      

solution = Solution()
result = solution.isPalindrome(-121)