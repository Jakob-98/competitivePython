#https://leetcode.com/problems/add-two-numbers/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0 
        longest = "x"
        sub = ""
        for char in s: 
            if char not in sub: 
                sub += char
            else: 
                sub = sub[sub.find(char)+1:]
                sub += char
            if len(sub) > len(longest):
                longest = sub
        return len(longest)
                