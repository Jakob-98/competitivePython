#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I'       :      1,
            'V'       :      5,
            'X'       :      10,
            'L'       :      50,
            'C'       :      100,
            'D'       :      500,
            'M'       :      1000
        }
        out = 0
        for i in range(len(s)-1):
            if vals.get(s[i]) < vals.get(s[i+1]):
                out -= vals.get(s[i])
            else:
                out += vals.get(s[i])
        out += vals.get(s[-1])    
        return out