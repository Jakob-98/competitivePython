#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        reverse = int()
        if x > 0: 
            reverse = int(str(x)[::-1])
        else: 
            reverse =  int('-' + (str(abs(x))[::-1]))
        if reverse > 2**31 or reverse < -2**31:
            return 0 
        return reverse
