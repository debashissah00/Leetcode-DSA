from typing import List

# horizontal scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Update the prefix by comparing it with each string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:
                    return ""
        
        return prefix

# vertical scanning
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(len(prefix)):
            ch = prefix[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix[:i]
        return prefix
    
sol = Solution1()
# print(sol.longestCommonPrefix(["test", "t", "tension"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))