class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        counters = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counters] = nums[i]
                counters += 1
        return counters

sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2],2))