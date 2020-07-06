#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if not strs[0]: return ""
        pref = []
        check = [strs[0][0]]
        try:
            while True:
                for i, word in enumerate(strs):
                    if word[len(check)-1] == check[len(check)-1]:
                        continue
                    else:
                        return ''.join(pref)
                pref.append(check[len(check)-1])
                check.append(strs[0][len(check)])
        except IndexError: 
            return ''.join(pref)
            
        
                