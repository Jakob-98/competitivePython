from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        count = Counter(s)
        for i, key in enumerate(count):
            if count[key] == 1:
                return i
        return -1