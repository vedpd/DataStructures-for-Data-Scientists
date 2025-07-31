class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Approach 1
        # nums= sorted(nums,reverse=True)
        # return nums[k-1]

        #Approach 2
        import heapq
        a= heapq.nlargest(k,nums)
        return a[k-1]