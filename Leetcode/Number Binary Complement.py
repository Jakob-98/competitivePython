#https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        comp = lambda c: '1' if c=='0' else '0'
        return int("".join(list(map(comp, list(bin(num)[2:])))),2)
