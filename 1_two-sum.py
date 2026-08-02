#Question: https://leetcode.com/problems/two-sum/

from typing import List

# Brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i] + nums[j+1]) == target: 
                    return [i, j+1]

# Two pass hash table solution                
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

# One pass hash table solution
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

# sol = Solution2()
# print(sol.twoSum([2, 3, 4, 5], 8))












class Sol1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2 hash
        mapp = {} #{2:0, 3:1, 4:2, 5:3}
        for i in range(len(nums)):
            mapp[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapp and i != mapp[comp]:
                return [i,mapp[comp]] 

class Sol2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1 hash
        mapp = {}

        for i in range(len(nums)):
            comp  = target - nums[i]
            if comp in mapp:
                return [mapp[comp], i]
            mapp[nums[i]] = i    
                    

s1 = Sol2()
print(s1.twoSum([3, 2, 5, 4], 6))




