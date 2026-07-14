def quickSort(nums) -> List[int]:
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x < pivot ]
    middle = [x for x in nums if x == pivot ]
    right = [x for x in nums if x > pivot ]
    return quickSort(left) + middle + quickSort(right)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortNums = quickSort(nums)
        for i in range(len(sortNums)-1):
            if sortNums[i] == sortNums[i+1]:
                return True
        return False
        
nums = [3,4,1,7,0,-1,-2]
sol = Solution()
sol.hasDuplicate(nums)