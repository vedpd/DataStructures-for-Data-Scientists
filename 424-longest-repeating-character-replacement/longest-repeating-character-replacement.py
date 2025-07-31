class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # count={}
        # res =0

        # for r in range(len(s)):
        #     #updating the hashmap
        #     count[s[r]] = 1 + count.get(s[r],0)
        #     # running a while loop to validate the window
        #     # window works if: window size - most frequent <=k
        #     # for case where it is greater than k, then we need to update left
        #     window_size = r - l + 1
        #     max_freq = max(count.values())

        #     while (window_size - max_freq) > k :
        #         count[s[l]] -= 1
        #         l += 1
            
        #     res = max(res,window_size)
        
        # return res

        count={}
        res= 0
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res= max(res,r-l+1)
        
        return res

        