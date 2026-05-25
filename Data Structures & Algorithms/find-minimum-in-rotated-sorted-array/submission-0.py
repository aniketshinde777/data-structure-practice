class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

'''
4 5 6 7

3,4,5,6,1,2
3 < 6 -> 3 + 6 -> 9 // 2 -> 5
r = 4 
3 + 4 = 7 // 2 -> 3 

m = 6
if 6 < 1
    m = r
else 
     l = mid + 1 = 3 idx -> 4

'''
        