class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                for j in range(len(nums)):
                    if nums[j] == diff:
                        return [j,i]
            else:
                seen.add(nums[i])

nums = [12,95,5,0,-2,4,9]
target = 10
sol = Solution()
print(sol.twoSum(nums, target))