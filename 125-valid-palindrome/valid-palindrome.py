# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr= ""
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
        
#         return newStr == newStr[::-1]

#Two pointer approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        left = 0 
        right = len(string) - 1
        string = string.lower()
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        