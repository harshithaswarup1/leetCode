import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        pattern = re.compile(r'^[0-9]+$|^[a-zA-Z]+$')
        rev_list = []
        oldlist = []
        string = s[::-1]
        for y in s:
            if pattern.match(y):
                oldlist.append(y)
        oldlist = ''.join(oldlist)
        for x in string:
            if pattern.match(x):
                rev_list.append(x)
        reveresed_list = ''.join(rev_list)
        if (oldlist == reveresed_list):
            return True
        else:
            return False
solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")