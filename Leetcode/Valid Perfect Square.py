#https://leetcode.com/problems/valid-perfect-square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i*i <= num:
            i+=1
            if i * i == num:
                return True
        return False