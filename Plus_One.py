class Solution(object):
    def plusOne(self, digits):
        if digits != []:
            digilist = ''.join(map(str, digits))
            new_num = int(digilist) + 1
            new_list = list(map(int, str(new_num))) 
            return new_list
solution = Solution()
result = solution.plusOne([9,0])