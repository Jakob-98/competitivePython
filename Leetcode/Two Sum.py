#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i, e in enumerate(nums):
            if target - e in dict: 
                return [i, dict.get(target - e)]
           
            dict[e] = i
