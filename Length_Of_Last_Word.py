class Solution(object):
    def lengthOfLastWord(self, s):
        actual_list = s.split(' ')
        new_list = []
        for string in actual_list:
            if string != '':
                new_list.append(string)
        return len(new_list[-1])
solution = Solution()
result = solution.lengthOfLastWord("   fly me   to   the moon  ")