#Question: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x2 = x
        rev = 0
        if x < 0:
            return False
        else:
            while x2 != 0:
                rev = rev*10 + (x2%10)
                x2 = x2//10
            return rev == x
sol = Solution()
print(sol.isPalindrome(1221))
