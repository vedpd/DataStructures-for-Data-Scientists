class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + ((right - left)//2)

            #left neighbor greater than value at index mid
            if mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            
            #right neighbor greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            else:
                return mid


            # if nums[mid - 1] < nums[mid] and nums [mid + 1] < nums[mid]:
            #     return mid
            
            # elif nums[mid] < nums[mid + 1] and (mid + 1) is not None:
            #     left = mid + 1
            
            # else:
            #     right = mid -1
            
