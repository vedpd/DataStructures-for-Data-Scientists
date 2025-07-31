class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left,right):  #check for valid palindrome
            left, right = left, right
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check(left+1, right) or check(left, right - 1)

            left +=1
            right -= 1
        
        return True



        