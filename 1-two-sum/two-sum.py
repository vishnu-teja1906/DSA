class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls={}
        for i in range(len(nums)):
            if target - nums[i] in ls:
                return [ls[target-nums[i]],i]
            ls[nums[i]]=i