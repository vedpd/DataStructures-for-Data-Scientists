class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #tracking presence of element
        # charSet = set()
        # left = 0
        # right =0
        # result =0
        # for right in range(0,len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left += 1
            
        #     charSet.add(s[right])
        #     result= max(result, right - left + 1)
        
        # return result



        left = 0
        charSet=set()
        ans =0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            ans = max( ans, right - left + 1)
        
        return ans


            
        