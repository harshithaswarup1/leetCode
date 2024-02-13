class Solution(object):
    def findTheDifference(self, s, t):
        s_dict = {}
        t_dict = {}
        count = 0
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for chars in t:
            if chars in t_dict:
                t_dict[chars] += 1
            else:
                t_dict[chars] = 1
        for x in t_dict.keys():
            if x not in s_dict.keys() or t_dict[x] != s_dict[x]:
                print (x)
    
        
solution = Solution()
result = solution.findTheDifference("aa","aaa")