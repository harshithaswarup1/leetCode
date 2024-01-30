class Solution(object):
    def fizzBuzz(self, n):
        array_list=[]
        for i in range(1,n+1):
            if (i % 3 == 0 and i % 5 ==0):
                array_list.append("FizzBuzz")
            elif (i % 3 == 0):
                array_list.append("Fizz")
            elif (i % 5 ==0):
                array_list.append("Buzz")    
            else:
                array_list.append(str(i))
        return array_list
solution = Solution()
result = solution.fizzBuzz(15)