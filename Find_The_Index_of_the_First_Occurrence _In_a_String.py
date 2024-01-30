class Solution(object):
    def strStr(self, haystack, needle):
        if str(needle) in str(haystack):
            index = haystack.find(needle)
            return index
        else:
            return -1
solution = Solution()
result = solution.strStr("sadbutsad","sad")